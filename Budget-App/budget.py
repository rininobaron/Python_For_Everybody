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
	categories_percentage = {}
	for category in categories:
		categories_percentage[category.name] = category.name
		name = categories_percentage[category.name]
		total_amount = 0
		for dictionary in category.ledger:
			spent = 0
			total_amount += dictionary['amount']
			if dictionary['amount'] < 0:
				spent += dictionary['amount']
		categories_percentage[name] = int(round(spent/total_amount, 1)*100)
	'''
	BUILDING FINAL STRING
	'''
	for i in range(11):
		new_i = 100 - i*10
		spaces = int(3 - len(str(new_i)))*' ' 
		LINE = LINE + spaces + str(new_i) + '|' + '\n'
		for category in categories:
			if new_i <= categories_percentage[category.name]:
				LINE += 'o'
			else:
				LINE += '_' #CHANGE
	return LINE
