"""
exercise 5
"""
from exercise4 import divide
from calculator import add
import pytest
def test_divide_zero_division():
	with pytest.raises(ZeroDivisionError):
		divide(5,0)
def test_add_type_error():
	with pytest.raises(TypeError):
		add(5, "hello")
