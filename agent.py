from robot import Robot
import random as rand

class Agent:
	def __init__(self):
		self.robot = Robot()
		self.commands = {"up":self.robot.up(),
                         "left":self.robot.left(),
                         "down":self.robot.down(),
                         "right":self.robot.right(),
                         "clean":self.robot.clean()}

	def make_choice(self):
		return self.commands[rand.choice(["up", "left", "down", "right", "clean"])]
