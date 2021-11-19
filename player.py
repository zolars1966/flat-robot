from robot import Robot

class Player:
	def __init__(self):
		self.robot = Robot()

	def do(self, action):
		if action is "up":
			return self.robot.up()
		if action is "down":
			return self.robot.down()
		if action is "right":
			return self.robot.right()
		if action is "left":
			return self.robot.left()
		if action is "clean":
			return self.robot.clean()
