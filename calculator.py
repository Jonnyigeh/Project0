"""
Exercise 1, 2, 3
"""
def add(x, y):
	return x + y

def test_add():
	"""
	When using float numbers we check for equality by
	checking if the absolute value of the 
	difference is below a chosen tolerance
	"""
	tol = 1e-10
	a = 0.1
	b = 0.2
	c = "Hello "
	d = "World"
	assert abs(add(a, b) - 0.3) < tol and add(c, d) == "Hello World"


