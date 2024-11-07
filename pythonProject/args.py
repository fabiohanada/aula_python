def ex(*args):
    print(*args)
    total = 0
    for numeros in args:
        total = total + numeros
    return total



print(ex(1, 2))