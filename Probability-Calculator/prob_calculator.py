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
				if value == 0:
					continue
				else:
					for i in range(value):
						contents.append(key)
			self.contents = contents
			self.balls = sum(values)
			self.values = values
			self.contents2 = []

	def draw(self, balls_draw=None):
		balls = self.balls
		keys = self.keys
		values = self.values
		if not balls_draw:
			return 'No balls to draw'
		if balls_draw > balls:
			return self.contents
		arguments_temp = copy.deepcopy(self.arguments)
		tuples = list(self.arguments.items())
		tuples_temp = copy.copy(tuples)
		counter = 0
		temp = False
		hi = 0
		iteration = 0
		contents2 = []
		while counter < balls_draw:
			iteration += 1
			if len(self.contents) != sum(arguments_temp.values()):
				raise Exception('Error')
			if (len(self.contents) == sum(arguments_temp.values())) and (sum(arguments_temp.values()) > 0):
				try:
					index = random.randint(0, len(self.contents) - 1)
					temp = self.contents[index]
					contents2.append(temp)
				except Exception as e:
					temp = False
					print('PASS')
					print(e)
					pass
			elif (len(self.contents) == sum(arguments_temp.values())) and (0 == sum(arguments_temp.values())):
				break
			if temp:
				self.contents.remove(temp)
				arguments_temp[temp] -= 1
				counter += 1
		contents_draw = []
		for (key, value_final) in list(arguments_temp.items()):
			value_draw = self.arguments[key] - value_final
			if value_draw == 0:
				continue
			string_temp = value_draw*(key+',')
			string_split = string_temp[:-1].split(',')
			for tag in string_split:
				contents_draw.append(tag)
		self.arguments = arguments_temp
		self.balls = sum(list(arguments_temp.values()))
		self.keys = list(arguments_temp.keys())
		self.values = list(arguments_temp.values())
		self.contents_draw = contents_draw
		self.contents2 = contents2
		return self.contents2

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	N = num_experiments
	M = 0
	for i in range(N):
		#print(i)
		temp = copy.deepcopy(hat)
		balls_drawn = temp.draw(num_balls_drawn)
		colors = []
		for color in expected_balls:
			color_drawn_count = 0
			for color_drawn in balls_drawn:
				if color_drawn == color:
					color_drawn_count += 1 
			if expected_balls[color] <= color_drawn_count:
				colors.append(color)
		if len(colors) == len(list(expected_balls.keys())):
			M += 1
	probability = M/N
	return probability