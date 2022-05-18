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
		values = self.values
		if not balls_draw:
			return 'No balls to draw'
		elif balls_draw > balls:
			return 'balls to draw are more than balls inside the hat'
		prob = balls_draw/balls
		values_temp = []
		for value in self.values:
			balls -= int(value*prob)
			values_temp.append(value - int(value*prob))
			print(value, prob, int(value*prob))
		balls_final = self.balls - balls_draw
		while balls > balls_final:
			for i in range(len(values_temp)):
				if balls == balls_final:
					break
				if values_temp[i] == 0:
					print('balls_final: ', str(balls_final))
					print('balls: ', str(balls))
					continue
				if values_temp[i] > 0:
					balls -=1
					values_temp[i] -= 1
					print('balls_final: ', str(balls_final))
					print('balls: ', str(balls))
		print('random probability (random number 0 to 1): ' + str(random.random()))
		print('balls_original: ' + str(self.balls))
		print('balls_final: ' + str(balls))
		print('values: ' + str(self.values))
		print('values_temp: ' + str(values_temp))

# Random Case for Testing
hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
print('balls: ' + str(hat.balls))
print(hat.draw(9))