import pytest

from utilspie import asyncutils


def test_async_call():
    """
    Test `async_call` for:
        * successful execution of passed function
        * raise Exception in case of exception in passed function
    """

    def test_function1(param1, param2, param3):
        return param1 + param2 + param3

    def test_function2(param1, param2, param3):
        return param1 + param2 + param3

    def test_function_raising_exception(param1, param2, param3):
        """Function to raise exception"""
        raise ValueError

    test_function_list = [
        (test_function1, (1, 3), {'param3': 4}),
        (test_function2, (2,), {'param2': 6, 'param3': 4}),
        (test_function1, (), {'param1': 9, 'param2': 10, 'param3': 4}),
        (test_function2, (4, 5, 6), {}),
    ]

    # Results of the functions with synchronous call
    function_results = [func(*args, **kwargs) for func, args, kwargs in test_function_list]

    # Results of the functions with asynchronous call
    async_function_results = asyncutils.async_call(test_function_list)

    # Test for success response for the async call
    for expected, result in zip(function_results, async_function_results):
        assert expected == result

    test_function_list_with_exception = test_function_list + [
        (test_function_raising_exception, (1, 5), {'param3': 3})
    ]

    # Check for raised exception in async functions
    with pytest.raises(ValueError):
        _ = asyncutils.async_call(test_function_list_with_exception)
