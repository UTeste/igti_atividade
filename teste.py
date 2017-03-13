import pytest
from main import somar
from main import subtrair

def teste_soma():
        """docstring for test somar"""
        assert somar(10,3) == 14

def teste_subtracao():
	"""docstring for test subtrair"""
	assert subtrair(11,7) == 4
