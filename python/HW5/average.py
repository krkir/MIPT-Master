count = []
with open("in.txt", "r") as f:
    for i in f:
        count.append(i.count("a"))
with open("out.txt", "w") as f1:
    f1.write(f"{sum(count) / len(count)}")