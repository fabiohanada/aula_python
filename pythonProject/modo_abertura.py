"""

with open('university.txt', 'w') as arquivo:
    arquivo.write('Teste2.\n')

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

"""
with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo\n')
    arquivo.write('Nova linha\n')
    arquivo.write('mais\n')

