def logger(file):
    def actual_dec(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file, "a") as f:
                f.write(f"{func.__name__}:{result}\n")
        return wrapper
    return actual_dec