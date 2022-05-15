class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return (self.width * self.height)

	def get_perimeter(self):
		return (2 * self.width + 2 * self.height)

	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** .5)
	def get_picture(self):
		if (self.width > 50) or (self.height > 50):
			return "Too big for picture."
		picture = ''
		for i in range(self.height):
			picture = picture + self.width*"*"
			picture = picture + '\n'
		return picture

	def get_amount_inside(self, shape_objet):
		'''OBJECT PARAMETERS'''
		#area_objet = shape_objet.get_area()
		perimeter_objet = shape_objet.get_perimeter()
		diagonal_objet = shape_objet.get_diagonal()
		width_object = shape_objet.width
		height_object = shape_objet.height
		'''SELF PARAMETERS'''
		#area = self.get_area()
		perimeter = self.get_perimeter()
		diagonal = self.get_diagonal()
		width = self.width
		height = self.height
		'''SOLUTION CASES'''
		if (height == height_object) and (width == width_object):
			return 1
		elif (height > height_object) and (width > width_object):
			y_number = int(height/height_object)
			x_number = int(width/width_object)
			return x_number*y_number
		else:
			return 0

	def __str__(self):
		if self.height == self.width:
			return "Square(" + "side="+ str(self.width) + ")" # or self.height
		else:
			return "Rectangle(" + "width=" + str(self.width) + ", " + "height=" + str(self.height) + ")"


class Square(Rectangle):

	def __init__(self, length):
		self.width = length
		self.height = length

	def set_side(self, side):
		self.width = side
		self.height = side

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height