"""
1 faca umprograma que receba dois numeros e mostre qual e o maior deles
"""

numero1: int = int(input("informe o 1 numero: "))
numero2: int = int(input("informe o 2 numero: "))

if numero1 > numero2:
    print(f"O numero {numero1} eh maior que {numero2}")
elif numero1 == numero2:
    print(f"os numeros {numero1} e {numero2} sao iguais")
else:
    print(f"o numero {numero2} eh maior que {numero1}")