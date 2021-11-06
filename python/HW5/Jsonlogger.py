import json

def jsonlogger(file):
    def actual_dec(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            dct = {"name" : func.__name__, "args" : args, "kwargs" : kwargs, "return" : result}
            with open(file, "a") as f:
                json.dump(dct, f)
                f.write("\n")
        return wrapper
    return actual_dec