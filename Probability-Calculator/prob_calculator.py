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
				print((key, value))
				if value == 0:
					continue
				else:
					for i in range(value):
						print('NUEVO')
						print(i)
						contents.append(key)
						print('GOOD')
						print('NUEVO FIN')
			self.contents = contents
			self.balls = sum(values)
			self.values = values
		print('len(self.contents): ',len(self.contents))
		print('self.')

	def draw(self, balls_draw=None):
		balls = self.balls
		keys = self.keys
		values = self.values
		if not balls_draw:
			return 'No balls to draw'
		if balls_draw > balls:
			return self.contents
		arguments_temp = copy.copy(self.arguments)
		print('in draw method len(self.contents): ', len(self.contents))
		tuples = list(self.arguments.items())
		tuples_temp = copy.copy(tuples)
		counter = 0
		#print(arguments_temp)
		temp = False
		hi = 0
		print('HI')
		print('len(self.contents): ',len(self.contents))
		print('sum(arguments_temp.values()): ',sum(arguments_temp.values()))
		print('Free Errors: ',len(self.contents) == sum(arguments_temp.values()))
		print()
		iteration = 0
		while counter < balls_draw:
			print('Condition while: ',counter < balls_draw)
			print('Free Errors: ',len(self.contents) == sum(arguments_temp.values()))
			print('iteration: ',iteration)
			iteration += 1
			if len(self.contents) != sum(arguments_temp.values()):
				print('Free Errors: ',len(self.contents) == sum(arguments_temp.values()))
				raise Exception('Error')
			print('counter: ', counter)
			print('balls_draw: ', balls_draw)
			print(len(self.contents))
			print(sum(arguments_temp.values()))
			if (len(self.contents) == sum(arguments_temp.values())) and (sum(arguments_temp.values()) > 0):
				try:
					index = random.randint(0, len(self.contents) - 1)
					temp = self.contents[index]
					print('temp: ',temp)
				except:
					temp = False
					print('STEP')
					continue
			elif len(self.contents) == sum(arguments_temp.values()):
				break
			if temp:
				#temp = random.choice(self.contents)
				print('TEMP EXISTS IN while')
				print('len(self.contents):                 ', len(self.contents))
				print('sum(list(arguments_temp.values())): ', sum(list(arguments_temp.values())))
				print(self.contents)
				self.contents.remove(temp)
				print(self.contents)
				print()
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
		print('FIN draw')
		return self.contents_draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	N = num_experiments
	M = 0
	for i in range(N):
		print('EXPERIMENT: ',i)
		print('hat.contents: ',hat.contents)
		temp = copy.deepcopy(hat)
		suma = 0
		for j in temp.arguments.values():
			suma += j
		print('suma', suma)
		print('temp.balls: ',temp.balls)
		print('sum(list(temp.arguments.values())): ', sum(list(temp.arguments.values())))
		print('len(temp.contents): ',len(temp.contents))
		print("ORIGINAL VALUES")
		print('temp.contents: ',temp.contents)
		print('num_balls_drawn: ',num_balls_drawn)
		temp.draw(num_balls_drawn)
		print("FINAL VALUES")
		print(temp.arguments)
		print(temp.balls)
		print()
		print()
		print()
		print()
		print()
		print()
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