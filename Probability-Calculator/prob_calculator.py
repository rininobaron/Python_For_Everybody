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
		balls_final = self.balls - balls_draw
		if not balls_draw:
			return 'No balls to draw'
		elif balls_draw > balls:
			return 'balls to draw are more than balls inside the hat'
		#prob = balls_draw/balls
		values_temp = []
		#random values abd tags
		values_random_temp = []
		arguments_random = sorted(self.arguments).
		keys_random = arguments_random.keys()
		values_random = arguments_random.values()
		for value in values_random:
			random_num = random.random()
			if balls < balls_final:
				break
			balls -= int(value*random_num)
			values_random_temp.append(value - int(value*random_num))
			print(value, random_num, int(value*random_num))
		for (key_r, value_r) in zip(keys_random, values_random_temp):
			for key in keys:
				if key == key_r:
					kddjdhkjd
					kdjkdj
				values_temp.append
		kjhjg
		kljkh
		lklkjk
		lkjkj
		while balls > balls_final:
			for i in range(len(values_temp)):
				if balls == balls_final:
					break
				if values_temp[i] == 0:
					print('balls_final: ', str(balls_final))
					print('balls: ', str(balls))
					continue
				if values_temp[i] > 0:
					balls -= 1
					values_temp[i] -= 1
					print('balls_final: ', str(balls_final))
					print('balls: ', str(balls))
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
			print(value_temp, ' new ', key,' tags was appended successfully!', )
		print('\n' + 'contents: ' + '\n' + str(contents))
		self.values_temp = values_temp # Add like attribute in order to use in function 'experiment'
		self.contents = contents
		return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	print(expected_balls)
	print(num_balls_drawn)
	print(num_experiments)
	print(hat.balls)
		




# Random Case for Testing
hat = Hat(red=5, orange=4, black=1, blue=0, piink=2, striped=9)
print('balls: ' + str(hat.balls))
print(hat.draw(9))
print(experiment(hat=hat, 
                  expected_balls={"red":2,"green":1}, 
                  num_balls_drawn=5, 
                  num_experiments=2000))