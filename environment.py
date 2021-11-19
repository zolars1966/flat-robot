import random as rand
import numpy as np
from player import Player


class Environment:
    def __init__(self, m, n):
        self.width, self.height = m, n
        self.flat = list()
        self.x, self.y = 0, 0 # rand.randint(0, m-1), rand.randint(0, n-1)
        self.agent = Player()
        self.fill()
    
    def fill(self):
        for i in range(self.width):
            line = list()
            for j in range(self.height):
                c = rand.randint(0, 1)
                if c:
                    color = [160, 160, 160]
                else:
                    color = [255, 255, 255]
                line.append(color)
            self.flat.append(line)
        self.flat = np.asarray(self.flat)

    def do(self, key):
        act = self.agent.do(key)
        if act == "clean":
            self.flat[self.x][self.y] = [255, 255, 255]
        else:
            self.x += act[0]
            self.y += act[1]
            self.x, self.y = min(self.width-1, max(0, self.x)), min(self.height-1, max(0, self.y))
