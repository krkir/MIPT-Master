import pickle
import json

with open("in", "rb") as r:
    f = pickle.load(r)
with open("out.txt", "w") as w:
    json.dump(f, w, indent=4, sort_keys=True)