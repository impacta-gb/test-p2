from calculadora import *

def test_multiplicacao():
    result = multiplicacao(7, 7)
    assert result == 49 

def test_soma():
    result = soma(4, 3)
    assert result == 7

def test_sub():
    result = sub(1, 3)
    assert result == -2 


def test_calculadora():
    result = calculadora(1, 3, 4)
    assert result == 12