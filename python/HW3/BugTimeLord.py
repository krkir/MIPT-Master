def print_count_debug(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        if DEBUG:
            print(count)
        return func(*args, **kwargs)
    return wrapper
