import pytest
from main import somar

def teste_soma():
        """docstring for test somar"""
        assert somar(10,3) == 13

def teste_subtrair():
	"""docstring for test subtrair"""
	assert subtrair(11,7) == 4
