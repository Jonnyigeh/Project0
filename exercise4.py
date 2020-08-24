"""
Test of various functions
"""
import math as m

def factorial(x):
	facto = 1
	for i in range(1, x+1):
		facto *= i
	return facto

def sin(x, N):
	sin = sum((-1)**N*x**(2*N+1)/factorial(2*N + 1) for N in range(N))
	return sin

def divide(x, y):
	return x/y
	
def f1(x, y):
	return x + y
def f2(x):
	return x**2

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
