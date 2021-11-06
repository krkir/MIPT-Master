from math import pi as pi

class Sphere:             

    def __init__(self):
        with open("in.txt") as f:
            self.r, self.x, self.y, self.z = f.readline().rstrip('\n').split()
        self.v = round(self.calc_V(), 2)
        self.write_it()

    def calc_V(self):
        return 4 / 3 * round(pi, 2) * (float(self.r) ** 3)


    def write_it(self):
        with open("out.txt", "w") as f:
            out = f"X: {self.x} \nY: {self.y} \nZ: {self.z} \nR: {self.r} \nVolume: {self.v}"
            f.write(out)

Sphere()