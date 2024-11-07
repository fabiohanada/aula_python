"""
numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'retorno: {ret_pop}')

from random import random

def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
"""

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(5, 3))
print(multiplica(2, 8))

print(outra(3, 2, 'fabio'))


