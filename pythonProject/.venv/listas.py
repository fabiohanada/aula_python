type([])

lista1 = [11, 99, 4, 27, 15]

lista2 = ['f', 'a', 'b', 'i', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list('fabio')
#
if 8 in lista4:
    print("encontrei")
else:
    print("nao encontrei")


#ordenar
lista1.sort()
print(lista1)

#contar
print(lista1.count(11))
print(lista5.count('f'))

#adicionar
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([3, 1])
print(lista1)

lista1.extend([23,76, 99])
print(lista1)

lista1.extend('fabio')
print(lista1)

lista1.insert(2, 'novo')
print(lista1)

lista6 = lista1 + lista2
print(lista6)

lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

print(len(lista1))

print(lista5)
lista5.pop()
print(lista5)

lista6 = lista2.copy()
print(lista6)

lista5.pop(2)
print(lista5)

print(lista5)
lista5.clear()
print(lista5)

print(lista6)

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

curso = 'fabio hanada'
print(curso)
curso = curso.split()
print(curso)