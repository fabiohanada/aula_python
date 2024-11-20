"""


debug

def dividir(a, b):
    try:
        return int(a) /  int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

l = lista
n = proxima linha
p = imprime variavel
c = continua a execucao

import pdb

nome = 'Fabio'
sobrenome = 'Hanada'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'programacao'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""



