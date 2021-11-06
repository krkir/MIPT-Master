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
        elif type(anVector) == float:
            for i in range(len(self.coord)):
                res.append(self.coord[i] * anVector)
            return Vector(res)
        
    def __round__(self, num=0):
        res = []
        for i in self.coord:
            res.append(round(i, num))
        return Vector(res)
    
    def lenght(self):
        return (self * self) ** 0.5
    
    def norm(self):
        return self * (1 / v1.lenght())
    
    def proj(self, anVector):
        res = anVector * ((self * anVector) / (anVector * anVector))
        return res

with open("in.txt", "r") as f:
    v1 = Vector([float(i) for i in f.readline().rstrip('\n').split()])
    v2 = Vector([float(i) for i in f.readline().rstrip('\n').split()])

l = v1.lenght()
norm = v1.norm()
proj = v1.proj(v2)
with open("out.txt", "w") as f:
    print(round(l, 2), file=f)
    print(*round(norm, 2).coord, file=f)
    print(*round(proj, 2).coord, file=f)