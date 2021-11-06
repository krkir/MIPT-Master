id1_2, id2_3, id1_3 =[], [], []
with open("in.txt", "r") as f:
    next(f)
    line = f.readline()
    while line != "id2 -> id3\n":
        id1, id2 = line.split()
        id1_2.append((id1, id2))
        line = f.readline()
    line = f.readline()
    while line:
        id2, id3 = line.split()
        id2_3.append((id2, id3))
        line = f.readline()
for i in id1_2:
    for j in id2_3:
        if i[1] == j[0]:
            id1_3.append((i[0], j[1]))
id1_3 = sorted(id1_3)
with open("out.txt", "w") as f:
    f.write("id1 -> id3\n")
    for i in id1_3:
        f.write(f"{i[0]} {i[1]}\n")