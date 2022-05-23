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
			self.arguments = arguments # Add like attribute in order to use in method 'draw'
			contents = []
			balls = 0
			items = list(arguments.items())
			self.keys = list(arguments.keys()) # Add like attribute in order to use method 'draw'
			values = list(arguments.values())
			for (key, value) in items:
				for i in range(value):
					contents.append(key)
			self.contents = contents
			self.balls = sum(values)
			self.values = values

	def draw(self, balls_draw=None):
		balls = self.balls
		keys = self.keys
		values = self.values
		if not balls_draw:
			return 'No balls to draw'
		elif balls_draw > balls:
			return self.contents
		arguments_temp = copy.copy(self.arguments)
		tuples = list(self.arguments.items())
		tuples_temp = copy.copy(tuples)
		counter = 0
		print(arguments_temp)
		while counter < balls_draw:
			temp = random.choice(tuples_temp)
			key = temp[0]
			if arguments_temp[key] > 0:
				arguments_temp[key] -= 1
				counter += 1
			elif sum(arguments_temp.values()) == 0:
				break
			else:
				continue
		print(arguments_temp)
		contents_draw = []
		for (key, value_final) in list(arguments_temp.items()):
			value_draw = self.arguments[key] - value_final
			print('self.arguments[key]: ', self.arguments[key])
			print('value_final: ', value_final)
			print(value_draw)
			if value_draw == 0:
				continue
			string_temp = value_draw*(key+',')
			string_split = string_temp[:-1].split(',')
			for tag in string_split:
				contents_draw.append(tag)
		self.arguments = arguments_temp
		self.balls = sum(arguments_temp.values())
		self.keys = list(arguments_temp.keys())
		self.values = list(arguments_temp.values())
		contents = []
		for (key, value) in list(self.arguments.items()):
				for i in range(value):
					contents.append(key)
		self.contents = contents
		self.contents_draw = contents_draw
		return self.contents_draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	N = num_experiments
	M = 0
	for i in range(N):
		temp = copy.copy(hat)
		temp.draw(num_balls_drawn)
		colors = []
		for color in expected_balls:
			try:
				if expected_balls[color] == temp.arguments[color]:
					colors.append(color)
				else: 
					break
			except:
				break
		if len(colors) == len(list(expected_balls.keys())):
			M += 1
	return M/N



hat = Hat(red=5,blue=2)
actual = hat.draw(2)
print(actual)