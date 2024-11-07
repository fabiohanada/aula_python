"""
filter


"""

import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print(f'Media: {media}')

res = filter(lambda valor: valor > media, dados)
print(list(res))