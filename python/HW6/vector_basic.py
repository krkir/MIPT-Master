class Vector:
    def __init__(self, coord):
        self.coord = coord
    
    def __add__(self, anVector):
        res = []
        for i in range(len(self.coord)):
            res.append(self.coord[i] + anVector.coord[i])
        return Vector(res)
    
    def __sub__(self, anVector):
        res = []
        for i in range(len(self.coord)):
            res.append(self.coord[i] - anVector.coord[i])
        return Vector(res)
    
    def __mul__(self, anVector):
        res = []
        if type(anVector) == Vector:
            for i in range(len(self.coord)):
                res.append(self.coord[i] * anVector.coord[i])
            return sum(res)
        elif type(anVector) == int:
            for i in range(len(self.coord)):
                res.append(self.coord[i] * anVector)
            return Vector(res)
        
    def __round__(self, num=0):
        res = []
        for i in self.coord:
            res.append(round(i, num))
        return Vector(res)

with open("in.txt", "r") as f:
    v1 = Vector([int(i) for i in f.readline().rstrip('\n').split()])
    v2 = Vector([int(i) for i in f.readline().rstrip('\n').split()])
    num = int(f.readline().rstrip('\n'))

add = v1 + v2
sub = v1 - v2
mul_d = v1 * num
scalar = v1 * v2
with open("out.txt", "w") as f:
    print(*round(add, 2).coord, file=f)
    print(*round(sub, 2).coord, file=f)
    print(*round(mul_d, 2).coord, file=f)
    print(round(scalar, 2), file=f)