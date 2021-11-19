import random as rand


class Environment:
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.flat = list()
        self.r_y, self.r_x = rand.randint(0, m-1), rand.randint(0, n-1)
        self.fill()
    
    def fill(self):
        for i in range(self.m):
            line = list()
            for j in range(self.n):
                line.append(rand.randint(0, 1))
            self.flat.append(line)
