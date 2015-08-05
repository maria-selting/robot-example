class Product(object):
	price=0
	count=0
	tax=1

	def __init__(self, price, count, tax):
		self.price=price
		self.count=count
		self.tax=tax

	def price_with_tax(self):
		total=self.price * self.count*self.tax
		if self.price>500:
			return 0.9*total
		else:
			return total


products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]
total=0
for product in products:
	total+=product.price_with_tax()

print total