"""


def soma(numero1, numero2):
    valor_somado = numero1 + numero2
    return valor_somado

valor = soma(12, 12)

print(valor)

"""
def f(n):
    if n < 3:
        return n - 1
    else:
        return f(n-2) + f(n-1)
valor = f(10)

print(valor)