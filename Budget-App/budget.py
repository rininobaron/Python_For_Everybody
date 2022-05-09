class Category:

	def __init__(self, Name):
		self.name = Name
		self.ledger = []

	def deposit(self, amount, description = ''):
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description = ''):
		if self.check_funds(amount):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		else:
			return False

	def get_balance(self):
		total_amount = 0
		for dictionary in self.ledger:
			total_amount += dictionary["amount"]
		return total_amount

	def transfer(self, amount, category_object):
		if self.check_funds(amount):
			self.withdraw(amount, "Transfer to " + category_object.name)
			category_object.deposit(amount, "Transfer from " + self.name)
			return True
		else:
			return False

	def check_funds(self, amount):
		if amount > self.get_balance():
			return False
		else:
			return True

	def __str__(self):
		if (len(self.name)%2) == 0:
			asterix_per_side = int((30 - len(self.name))/2)
			line1 = asterix_per_side*'*' + self.name + asterix_per_side*'*'
		else:
			asterix_per_side = int((30 - len(self.name) + 1)/2)
			line1 = (asterix_per_side - 1)*'*' + self.name + asterix_per_side*'*'
		line1 = line1 + '\n'
		line_descriptions = ''
		for dictionary in self.ledger:
			if len(dictionary["description"]) <= 23:
				spaces = (23 - len(dictionary["description"]))*' '
				line_descriptions = line_descriptions + dictionary["description"] + spaces
			else:
				line_descriptions = line_descriptions + dictionary["description"][:23]
			if len('%.2f'%(dictionary["amount"])) <= 7:
				line_descriptions = line_descriptions + (7 - len('%.2f'%(dictionary["amount"])))*' ' + '%.2f'%(dictionary["amount"])
			else:
				line_descriptions = line_descriptions + '%.2f'%(dictionary["amount"])[-7:]
			line_descriptions = line_descriptions + '\n'
		final_line =  "Total: " + str(self.get_balance())
		return line1 + line_descriptions + final_line


def create_spend_chart(categories):
	LINE = 'Percentage spent by category\n'
	'''
	RETRIEVING CATEGORIES AND CALCULATING PERCENTAGES
	'''
	categories_spent = {}
	total_amount = 9 # ALL CATEGORIES
	for category in categories:
		categories_spent[category.name] = 0
		spent = 0
		for dictionary in category.ledger:
			if dictionary['amount'] < 0:
				total_amount += abs(dictionary['amount'])
				spent += abs(dictionary['amount'])
		categories_spent[category.name] = spent
		#print(categories_percentage[name])
	categories_percentage = {}
	for category_name in categories_spent:
		ratio = categories_spent[category_name]/total_amount
		ratio_str = str(ratio)
		ratio_str_list = ratio_str.split('.')
		ratio_str_final = ratio_str_list[0] + '.' + ratio_str_list[1][0]
		print(ratio_str_list[1][0])
		print(ratio_str_list)
		categories_percentage[category_name] = int(float(ratio_str_final)*100)
		print(categories_percentage[category_name])
		print(ratio_str_final)
		print('hola')
	'''
	BUILDING FINAL STRING
	'''
	for i in range(11):
		new_i = 100 - i*10
		spaces = int(3 - len(str(new_i)))*' ' 
		LINE = LINE + spaces + str(new_i) + '| '
		for category in categories:
			if new_i <= categories_percentage[category.name]:
				LINE = LINE + 'o  '
			else:
				LINE = LINE + '   '
		LINE = LINE + '\n'
	LINE = LINE + 4*' ' + '-'*int(len(categories)*3 + 1) + '\n'
	len_names = []
	for category in categories:
		len_names.append(len(category.name))
	last = max(len_names)
	for i in range(last):
		LINE = LINE + 5*' '
		for category in categories:
			try:
				LINE = LINE + category.name[i] + '  '
			except:
				LINE = LINE + '   '
			if ((i + 1) == last) and ((categories.index(category) + 1) == len(categories)):
				continue
			if (categories.index(category) + 1) == len(categories):
				LINE = LINE + '\n'
	return LINE