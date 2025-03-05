from io import StringIO

mensagem = 'string normal!!!!!'

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write('outro')

arquivo.seek(0)

print(arquivo.read())