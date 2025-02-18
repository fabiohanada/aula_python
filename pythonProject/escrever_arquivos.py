"""

with open('texto.txt', 'w') as arquivo:
    arquivo.write('escre eh facil.\n')
    arquivo.write('podemos.\n')
    arquivo.write('ultima')


arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('mais')

arquivo.close()


with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('informe uma fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



