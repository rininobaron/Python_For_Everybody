class Category:

	def __init__(self, Name):
		self.name = Name
		self.ledger = []

	def deposit(self, amount, description):
		if description = False:
			description = ""
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description):
		if description = False:
			description = ""
		if self.check_funds(amount):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		else:
			return False

	def get_balance(self):
		total_amount = 0
		for dictionary in self.lesdger:
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
		if len(self.name%2) == 0:
			asterix_per_side = (30 - len(self.name%2))/2
			line1 = asterix_per_side*'*' + self.name + asterix_per_side*'*'
		else:
			asterix_per_side = (30 - len(self.name%2) + 1)/2
			line1 = (asterix_per_side - 1)*'*' + self.name + asterix_per_side*'*'
		line1 = line1 + '\n'
		line_descriptions = ''
		total = 0
		for dictionary in self.ledger:
			if  len(dictionary["description"]) <= 23:
				spaces = (23 - len(dictionary["description"]))*' '
				line_descriptions = line_descriptions + spaces
			else:
				line_descriptions = line_descriptions + dictionary["description"][:23]
			if len('%.2f'%(dictionary["amount"])) <= 7:
				line_descriptions = line_descriptions + (7 - len('%.2f'%(dictionary["amount"])))*' ' + '%.2f'%(dictionary["amount"])
			else:
				line_descriptions = line_descriptions + '%.2f'%(dictionary["amount"])[-7:]
			line_descriptions = line_descriptions + '\n'
		final_line =  "Total: " + str(self.get_balance())
		return line1 + line_descriptions + final_line


#def create_spend_chart(categories):