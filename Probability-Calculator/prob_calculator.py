import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **arguments):
		if not arguments:
			self.balls = 1 # default
			self.contents = ['default']
			self.values = [1]
		else:
			contents = []
			balls = 0
			items = list(arguments.items())
			keys = list(arguments.keys())
			values = list(arguments.values())
			#print(contents)
			counter = 0
			for (key, value) in items:
				for i in range(value):
					contents.append(key)
			print(contents)
			# 	#if counter == 0:
			# 		#ksjssk
			# 	counter += 1
			# 	values.append(value)
			# 	balls += value
			self.contents = contents
			self.balls = sum(values)
			self.values = values
		print(self.balls)
		print(self.contents)
			
	def draw(self, balls_draw=None):
		if not balls_draw:
			return 'No balls to draw'
		elif balls_draw > self.balls:
			return 'balls to draw are more than balls inside the hat'
		print(balls_draw)
		print(random.random()*(balls_draw/self.balls))



# Random Case for Testing
hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
print(hat.draw(8))
