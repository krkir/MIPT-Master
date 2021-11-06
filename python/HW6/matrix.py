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
        elif type(anVector) == float or type(anVector) == int:
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
        return self * (1 / self.lenght())
    
    def proj(self, anVector):
        res = anVector * ((self * anVector) / (anVector * anVector))
        return res
    
    def __str__(self):
        res = ' '.join(str(e) for e in self.coord)
        return res

class Matrix:
    def __init__(self, vectors):
        self.vectors = vectors
    
    def __mul__(self, anMatrix):
        res = []
        for i in self.vectors:
            cur_vec = []
            for j in anMatrix.trans().vectors:
                cur_vec.append(i * j)
            vec_ = Vector(cur_vec)
            res.append(vec_)
        return Matrix(res)
    
    def trans(self):
        new_vec = []
        for i in range(len(vectors[0].coord)):
            cur_vec = []
            for j in range(len(self.vectors)):
                cur_vec.append(self.vectors[j].coord[i])
            vec_ = Vector(cur_vec)
            new_vec.append(vec_)
        return Matrix(new_vec)
    
    def __str__(self):
        res = "\n".join(str(e) for e in self.vectors)
        return res

vectors = []
m1 = input().split()
v = Vector([int(i) for i in m1])
vectors.append(v)
for i in range(len(m1) - 1):
    m2 = input().split()
    v = Vector([int(i) for i in m2])
    vectors.append(v)


m = Matrix(vectors)
print(m.trans())
print(m*m)