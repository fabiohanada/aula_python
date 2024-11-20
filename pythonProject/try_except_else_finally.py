"""

toda entrada de dados deve ser tratada

num = 0

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
print(f'Voce digitou {num}')

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Voce nao digitou um valor valido')
else:
    print(f'Voce digitou o numero {num}')
finally:
    print('Executando o finally')
"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Nao e possivel dividir por zero'

num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))


