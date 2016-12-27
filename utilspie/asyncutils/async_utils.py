from multiprocessing import Process, Queue


def async_call(func_list):
    """
    Runs the list of function asynchronously, returns the response maintaining the order

    :param func_list: Expects list of lists to be of format
        [[func1, args1, kwargs1], [func2, args2, kwargs2], ...]
    :return: List of output of the functions
        [output1, output2, ...]
    """

    def worker(function, f_args, f_kwargs, queue, index):
        """
        Runs the function and appends the output to list, and the Exception in the case of error
        """
        response = {
            'index': index,  # For tracking the index of each function in actual list.
            # Since, this function is called asynchronously, order in
            # queue may differ
            'data': None,
            'error': None
        }

        # Handle error in the function call
        try:
            response['data'] = function(*f_args, **f_kwargs)
        except Exception as e:
            response['error'] = e  # send back the exception along with the queue

        queue.put(response)

    queue = Queue()   # For preserving state across threads
    processes = [Process(target=worker, args=(func, args, kwargs, queue, i)) \
                 for i, (func, args, kwargs) in enumerate(func_list)]

    for process in processes:
        process.start()

    response_list = []
    for process in processes:
        # Wait for process to finish
        process.join()

        # Get back the response from the queue
        response = queue.get()
        if response['error']:
            raise response['error']  # Raise exception if the function call failed
        response_list.append(response)

    return [content['data'] for content in sorted(response_list, key=lambda x: x['index'])]
