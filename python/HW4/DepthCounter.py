def depthcounter(func):
    def reset():
        wrapper.rdepth = 0
        wrapper.ncalls = 0
        
    def wrapper(*args, **kwargs):
        if wrapper.depth == 0:
            reset()
        wrapper.ncalls += 1
        wrapper.depth += 1
        wrapper.rdepth = max(wrapper.rdepth, wrapper.depth)
        result = func(*args, **kwargs)
        wrapper.depth -= 1
        return result
    
    wrapper.depth = 0
    reset()
    return wrapper