def call_count(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return func(*args, **kwargs)
    return wrapper
