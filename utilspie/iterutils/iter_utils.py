

def get_chunks(list_obj, chunk_size=1):
    chunk_size = max(1, chunk_size)
    return (list_obj[i:i+chunk_size] for i in range(0, len(list_obj), chunk_size))
