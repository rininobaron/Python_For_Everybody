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
			#print(contents)
			counter = 0
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
		balls_final = self.balls - balls_draw
		#prob = balls_draw/balls
		values_temp = []
		#random values abd tags
		values_random_temp = []
		arguments_random_list = sorted(self.arguments)
		arguments_random = {}
		for key in arguments_random_list:
			arguments_random[key] = self.arguments [key] 
		keys_random = arguments_random.keys()
		values_random = arguments_random.values()
		for value in values_random:
			if value == 0:
				values_random_temp.append(value)
				continue
			random_num = random.random()
			balls -= int(value*random_num)
			if balls < balls_final:
				balls += int(value*random_num)
				values_random_temp.append(value)
			else:
				values_random_temp.append(value - int(value*random_num))
		'''WORKING'''
		if not len(values_random_temp) == len(values):
			return print('ERROR1')
		if sum(values_random_temp) == balls:
			pass
		else:
			print('sum(values_random_temp): ', sum(values_random_temp))
			print('balls: ', balls)
			return print("ERROR")
		'''WORKING'''
		if balls > balls_final:
			while balls > balls_final:
				if balls == balls_final:
					break
				for i in range(len(values_random_temp)):
					if balls == balls_final:
						break
					if values_random_temp[i] == 0:
						continue
					if values_random_temp[i] > 0:
						balls -= 1
						values_random_temp[i] -= 1
		'''REARRANGE values_temp ACCORDING TO ORIGINAL values'''
		for key in keys:
			for (key_r, value_r) in zip(keys_random, values_random_temp):
				if key == key_r:
					values_temp.append(value_r)
		contents = []
		for value, value_temp, key in zip(values, values_temp, self.keys):
			if value_temp == 0:
				continue
			string_temp = value_temp*(key+',')
			string_split = string_temp[:-1].split(',')
			for tag in string_split:
				contents.append(tag)
		'''UPDATING ATTRIBUTES'''
		arguments = {}
		for key, value in zip(keys, values_temp):
			arguments[key] = value
		'''
		FIXING LOGICAL PROBLEM

		The method returns the contents list, 
		but the method must return only 
		a list with the balls draw to the hat
		'''
		values_draw = [(i - temp) for i, temp in zip(self.values, values_temp)]
		contents_draw = []
		for value_draw, key in zip(values_draw, self.keys):
			if value_draw == 0:
				continue
			string_temp = value_draw*(key+',')
			string_split = string_temp[:-1].split(',')
			contents_draw = [tag for tag in string_split]
		self.arguments = arguments
		self.balls = balls
		self.keys = keys
		self.values = values_temp
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