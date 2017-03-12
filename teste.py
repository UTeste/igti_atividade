import pytest
from main import somar

def teste_da_soma():
        """docstring for test somar"""
        assert somar(10,3) == 13
