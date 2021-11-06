import csv
import json

with open('in.txt', "r") as csvfile:
    data = csv.DictReader(csvfile)
    dct = dict()
    for k in data.fieldnames:
        dct[k] = []
    for i in data:
        for item in i.items():
            dct[item[0]].append(int(item[1]))
with open("out.txt", "w") as w:
    json.dump(dct, w, indent=4, sort_keys=True)