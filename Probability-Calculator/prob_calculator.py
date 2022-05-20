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
			print(contents)
				# #if counter == 0:
				# 	#ksjssk
				# counter += 1
				# values.append(value)
				# balls += value
			self.contents = contents
			self.balls = sum(values)
			self.values = values
		print(self.balls)
		print(self.contents)

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
			arguments_random[key] = self.arguments[key] 
		keys_random = arguments_random.keys()
		values_random = arguments_random.values()
		for value in values_random:
			random_num = random.random()
			balls -= int(value*random_num)
			if balls < balls_final:
				balls += int(value*random_num)
				break
			values_random_temp.append(value - int(value*random_num))
			print(value, random_num, int(value*random_num))
		if balls <= balls_final:
			pass
		elif balls > balls_final:
			while balls > balls_final:
				if balls == balls_final:
					break
				for i in range(len(values_random_temp)):
					if balls == balls_final:
						break
					if values_random_temp[i] == 0:
						print('balls_final: ', str(balls_final))
						print('balls: ', str(balls))
						continue
					if values_random_temp[i] > 0:
						balls -= 1
						values_random_temp[i] -= 1
						print('balls_final: ', str(balls_final))
						print('balls: ', str(balls))
		'''REARRANGE values_temp ACCORDING TO ORIGINAL values'''
		for key in keys:
			for (key_r, value_r) in zip(keys_random, values_random_temp):
				if key == key_r:
					values_temp.append(value_r)
		print('random probability (random number 0 to 1): ' + str(random.random()))
		print('balls_original: ' + str(self.balls))
		print('balls_final: ' + str(balls))
		print('values: ' + str(self.values))
		print('values_temp: ' + str(values_temp))
		contents = []
		print()
		print()
		print(self.contents)
		for value, value_temp, key in zip(values, values_temp, self.keys):
			print(value, value_temp, key)
			if value_temp == 0:
				continue
			string_temp = value_temp*(key+',')
			print(string_temp[:-1])
			string_split = string_temp[:-1].split(',')
			for tag in string_split:
				contents.append(tag)
			print(value_temp, ' new ', key,' tags was appended successfully!')
		print('\n' + 'contents: ' + '\n' + str(contents))
		'''UPDATING ATTRIBUTES'''
		arguments = {}
		for key, value in zip(keys, values_temp):
			arguments[key] = value
		self.arguments = arguments
		self.balls = balls
		self.keys = keys
		self.values = values_temp
		self.contents = contents
		return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	for i in expected_balls:
		print(i, expected_balls[i])
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


# Random Case for Testing
hat = Hat(red=20, orange=10, black=1, blue=0, pink=2, striped=9)
print('balls: ' + str(hat.balls))
print(hat.draw())
print()
print()
print(experiment(hat=hat, 
                  expected_balls={"red":2,"orange":1}, 
                  num_balls_drawn=5, 
                  num_experiments=8))