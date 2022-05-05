def arithmetic_arranger(aritmetic_problems, show_results = False):
	list_temp = []
	line1 = ''
	line2 = ''
	line3 = ''
	line4 = 'Aquí van los resultados'
	if len(aritmetic_problems) > 5:
		#raise ValueError("Error: Too many problems.")
		return "Error: Too many problems."
	else:
		start_flag = False
		for i in aritmetic_problems:
			problem = i.split(" ")
			if problem[1] not in ['+', '-']:
				#raise ValueError("Error: Operator must be '+' or '-'.")
				return "Error: Operator must be '+' or '-'."
			for number in [problem[0], problem[2]]:
				for digit in number:
					if digit not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
						#raise ValueError("Error: Numbers must only contain digits.")
						return "Error: Numbers must only contain digits."
					elif len(number) > 4:
						#raise ValueError("Error: Numbers cannot be more than four digits.")
						return "Error: Numbers cannot be more than four digits."
			if start_flag == False:
				if len(problem[0]) > len(problem[2]):
					line1 = line1 + '  ' + problem[0]
					spaces = int(len(problem[0])) - int(len(problem[2]))
					line2 = line2 + problem[1] + ' ' + str(spaces*' ') + problem[2]
					line3 = (len(problem[0]) + 2)*'-'
					if problem[1] == '+':
						result = int(problem[0]) + int(problem[2])
					else:
						result = int(problem[0]) - int(problem[2])
					spaces2 = (len(problem[0]) + 2) - len(str(result))
					line4 = spaces2*' ' + str(result)
					start_flag = True
				elif len(problem[0]) < len(problem[2]):
					spaces = int(len(problem[2])) - int(len(problem[0]))
					line1 = line1 + '  ' + str(spaces*' ') + problem[0]
					line2 = line2 + problem[1] + ' ' + problem[2]
					line3 = (len(problem[2]) + 2)*'-'
					if problem[1] == '+':
						result = int(problem[0]) + int(problem[2])
					else:
						result = int(problem[0]) - int(problem[2])
					spaces2 = (len(problem[2]) + 2) - len(str(result))
					line4 = spaces2*' ' + str(result)
					start_flag = True
				else:
					line1 = line1 + '  ' + problem[0]
					line2 = line2 + problem[1] + ' ' + problem[2]
					line3 = (len(problem[0]) + 2)*'-'
					if problem[1] == '+':
						result = int(problem[0]) + int(problem[2])
					else:
						result = int(problem[0]) - int(problem[2])
					spaces2 = (len(problem[0]) + 2) - len(str(result))
					line4 = spaces2*' ' + str(result)
					start_flag = True
			else:
				if len(problem[0]) > len(problem[2]):
					line1 = line1 + str(4*' ') + '  ' + problem[0]
					spaces = int(len(problem[0])) - int(len(problem[2]))
					line2 = line2 + str(4*' ') + problem[1] + ' ' + str(spaces*' ') + problem[2]
					line3 = line3 + str(4*' ') + (len(problem[0]) + 2)*'-'
					if problem[1] == '+':
						result = int(problem[0]) + int(problem[2])
					else:
						result = int(problem[0]) - int(problem[2])
					spaces2 = (len(problem[0]) + 2) - len(str(result))
					line4 = line4 + str(4*' ') + spaces2*' ' + str(result)
				elif len(problem[0]) < len(problem[2]):
					spaces = int(len(problem[2])) - int(len(problem[0]))
					line1 = line1 + str(4*' ') + '  ' + str(spaces*' ') + problem[0]
					line2 = line2 + str(4*' ') + problem[1] + ' ' + problem[2]
					line3 = line3 + str(4*' ') + (len(problem[2]) + 2)*'-'
					if problem[1] == '+':
						result = int(problem[0]) + int(problem[2])
					else:
						result = int(problem[0]) - int(problem[2])
					spaces2 = (len(problem[2]) + 2) - len(str(result))
					line4 = line4 + str(4*' ') + spaces2*' ' + str(result)
				else:
					line1 = line1 + str(4*' ') + '  ' + problem[0]
					line2 = line2 + str(4*' ') + problem[1] + ' ' + problem[2]
					line3 = line3 + str(4*' ') + (len(problem[0]) + 2)*'-'
					if problem[1] == '+':
						result = int(problem[0]) + int(problem[2])
					else:
						result = int(problem[0]) - int(problem[2])
					spaces2 = (len(problem[0]) + 2) - len(str(result))
					line4 = line4 + str(4*' ') + spaces2*' ' + str(result)


	results = line1 + '\n' + line2 + '\n' + line3

	if show_results == True:
		results = results + '\n' + line4
		return results
	else:
		return results