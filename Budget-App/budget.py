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


def create_spend_chart(categories):

