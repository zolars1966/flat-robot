from robot import Robot
import random as rand

class Agent:
    def __init__(self):
        self.robot = Robot()
        self.commands = {"up":self.robot.up(),
                         "left":self.robot.left(),
                         "down":self.robot.down(),
                         "right":self.robot.right(),
                         "sit":self.robot.sit(),
                         "clean":self.robot.clean()}
        self.action = "sit"
        self.curr_task = "start"
        self.hdir = "down"

    def make_choice(self, view):

        if "dirty" in view:
            return self.commands["clean"]

        if "down" in view:
            self.hdir = "up"
        elif "up" in view:
            self.hdir = "down"
        
        if self.curr_task == "start":
            if "up" not in view:
                self.action = "up"
            elif "left" not in view:
                self.action = "left"
            else:
                self.curr_task = "force right wall"
                self.wdir = "right"
        elif self.curr_task == "force right wall":
            if "right" in view:
                self.curr_task = "left wall"
                self.action = self.hdir
            else:
                self.action = "right"
        elif self.curr_task == "left wall":
            if "left" in view:
                self.curr_task = "right wall"
                self.action = self.hdir
            else:
                self.action = "left"
        elif self.curr_task == "right wall":
            if "right" in view:
                self.curr_task = "left wall"
                self.action = self.hdir
            else:
                self.action = "right"

        return self.commands[self.action]
