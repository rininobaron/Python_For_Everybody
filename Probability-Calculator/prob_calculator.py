import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **arguments):
		if not arguments:
			self.balls = 1 # default
			self.contents = ['default']
		else:
			contents = []
			balls = 0
			list(arguments.items())
			for (key, value) in arguments.items():
				contents.append(key)
				values.append(value)
				balls += value
			self.contents = contents
			self.balls = balls

		print(self.balls)
		print(self.contents)
			
	def draw(self, balls):
		self.balls = balls