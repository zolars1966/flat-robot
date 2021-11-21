from pygame.locals import *
from robot import Robot
import pygame as pg

class Player:
    def __init__(self):
        self.robot = Robot()
        self.commands = {"up":self.robot.up(),
                         "left":self.robot.left(),
                         "down":self.robot.down(),
                         "right":self.robot.right(),
                         "clean":self.robot.clean()}

    def make_choice(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            return self.commands["up"]
        if keys[pg.K_a]:
            return self.commands["left"]
        if keys[pg.K_s]:
            return self.commands["down"]
        if keys[pg.K_d]:
            return self.commands["right"]
        if keys[pg.K_SPACE]:
            return self.commands["clean"]

        return "sit"
