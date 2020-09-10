import numpy as np
import calculator
import math as m
from calculator import add, factorial, sin, divide, f1, f2
"""
Exercise 1
"""
def test_add():
	assert (1 + 2) == 3

def test_add_float():
	"""
	When using float numbers we check for equality by
	checking if the absolute value of the
	difference is below a chosen tolerance
	"""
	tol = 1e-10
	a = 0.1
	b = 0.2
	assert abs(add(a, b) - 0.3) < tol

def test_add_strings():
	"""
	Checking that strings are added
	like expected
	"""
	a = "hello"
	b = " world"
	assert add(a,b) == "hello world"
"""
Exercise 4
"""
def test_factorial():
	assert factorial(5) == m.factorial(5)
def test_sin():
	tol = 1e-10
	assert abs(m.sin(0) - sin(0, 20)) < tol
def test_divide():
	tol = 1e-10
	a = 4
	b = 2
	assert abs(divide(4, 2) - 2) < tol
def test_f1():
	assert f1(2, 2) == 4
def test_f2():
	assert f2(2) == 4
"""
Exercise 5
"""
import pytest

def test_divide_zero_division():
	with pytest.raises(ZeroDivisionError):
		divide(5,0)
def test_add_type_error():
	with pytest.raises(TypeError):
		add(5, "hello")
"""
Exercise 6
Here we have the same testfunctions from task 1-4, but rewritten
on parametrized form as specified in exercise 6.
Did not include the last two testfunctions, as i didnt see
any reason to test for more than one type of error.
"""
@pytest.mark.parametrize("arg, eo", [[(1, 1), 2],[(2, 2), 4], [(3, 5), 8]])
def test_add(arg, eo):
	"""
	When using float numbers we check for equality by
	checking if the absolute value of the
	difference is below a chosen tolerance
	"""
	tol = 1e-10
	assert abs(add(arg[0], arg[1]) - eo) < tol

@pytest.mark.parametrize("x", [2, 3, 4])
def test_factorial(x):
	assert factorial(x) == m.factorial(x)

@pytest.mark.parametrize("x", [0, np.pi, 2*np.pi])
def test_sin(x):
	tol = 1e-10
	assert abs(m.sin(x) - sin(x, 20)) < tol

@pytest.mark.parametrize("arg, eo", [[(2, 2), 1], [(4, 2), 2], [(9,3), 3]])
def test_divide(arg, eo):
	tol = 1e-10
	assert abs(divide(arg[0], arg[1]) - eo) < tol

@pytest.mark.parametrize("arg, eo", [[(2, 2), 4], [(3, 3), 6]])
def test_f1(arg, eo):
	assert f1(arg[0], arg[1]) == eo

@pytest.mark.parametrize("x, x2", [(2, 4), (3, 9), (5, 25)])
def test_f2(x, x2):
	assert f2(x) == x2
