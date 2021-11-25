from player import Player
from agent import Agent
import random as rand
import numpy as np


class Environment:
    def __init__(self, m, n, r):
        self.width, self.height = m, n
        self.robots_num = r
        self.flat = list()
        self.agents = np.asarray([Agent() for _ in range(self.robots_num)])
        self.coords = [[0, 0] for _ in range(self.robots_num)]
        self.future_coords = [[0, 0] for _ in range(self.robots_num)]
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

        for i in range(self.width):
            for j in range(self.height):
                if i * self.height + j >= self.robots_num:
                    break
                self.coords[i * self.height + j] = [5, 6]
                self.future_coords[i * self.height + j] = [5, 6]

    def view(self, agent):
        view = []

        if np.array_equal(self.flat[self.coords[agent][0]][self.coords[agent][1]], np.asarray([160, 160, 160])):
            view.append("dirty")
        if self.coords[agent][0] - 1 < 0:
            view.append("left")
        if self.coords[agent][0] + 1 >= self.width:
            view.append("right")
        if self.coords[agent][1] - 1 < 0:
            view.append("up")
        if self.coords[agent][1] + 1 >= self.height:
            view.append("down")

        return view

    def check(self, agent, act):
        new_coord = [self.coords[agent][0] + act[0], self.coords[agent][1] + act[1]]
        new_coord[0], new_coord[1] = min(self.width-1, max(0, new_coord[0])), min(self.height-1, max(0, new_coord[1]))
        if new_coord not in self.coords:
            self.future_coords[agent] = new_coord

    def update(self):
        for agent in range(self.robots_num):
            view = self.view(agent)
            act = self.agents[agent].make_choice(view)
            if act == "clean":
                self.flat[self.coords[agent][0]][self.coords[agent][1]] = [255, 255, 255]
            elif act != "sit":
                self.check(agent, act)
                self.coords = self.future_coords
