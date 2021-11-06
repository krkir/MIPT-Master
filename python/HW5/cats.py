sum = 0
try:
    with open("in.txt", "r") as f:
        for line in f:
            sum += float(line)
except ValueError:
    with open("out.txt", "w") as f1:
        f1.write("nan")
else:
    with open("out.txt", "w") as f1:
        f1.write(f"{sum}")