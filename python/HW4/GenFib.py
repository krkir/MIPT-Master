def fibgen(f0, f1):
    while True:
        yield f0
        f0, f1 = f1, f0 + f1