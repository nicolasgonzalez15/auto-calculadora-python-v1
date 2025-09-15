import reloj
from stuff.calculadora import suma,resta,producto,division
import pytest

# Ingreso valores
def suma(nro1,nro2):
    return nro1+nro2

def test_sumar_positivo():
    assert suma(2, 3) == 5

def test_suma_con_fixture(numeros_enteros):
    a,b = numeros_enteros
    assert suma(a,b) == 15

