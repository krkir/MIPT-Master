class StringCount:
    def __init__(self):
        with open("in.txt", "r") as f:
            self.st = f.readline().rstrip('\n')
        self.a = self.count_a()
        
    def count_a(self):
        res = self.st.count('a') + self.st.count('A')
        with open("out.txt", "w") as f:
            f.write(str(res))
        return res


StringCount()