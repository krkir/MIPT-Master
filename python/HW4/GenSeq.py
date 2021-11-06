from random import choice

def genseq(alphabet, length):
    while True:
        seq = ''
        for i in range(length):
            seq += choice(alphabet)
        yield seq