coms = input().split(sep=";") 
exs = ["ArithmeticError", "LookupError", "OSError", "ValueError", "KeyError", "NameError", "FileExistsError" ,"ZeroDivisionError"]
for i in coms:
    try:
        exec(i)
        print(eval(i))
    except FileExistsError:
        print("FileExistsError")
    except KeyError:
        print("KeyError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except LookupError:
        print("LookupError")
    except ArithmeticError:
        print("ArithmeticError")
    except OSError:
        print("OSError")
    except ValueError:
        print("ValueError")
    except NameError:
        print("NameError")
    except Exception as ex:
        print("Other exception")
    except KeyboardInterrupt as kb:
        print("Other exception")