

def get_chunks(iterable_obj, chunk_size=1):
    chunk_size = max(1, chunk_size)
    return (iterable_obj[i:i+chunk_size] for i in range(0, len(iterable_obj), chunk_size))
