from random import choice
print("=" * 30)
print(" qual produto eu compro? ")
print("=" * 30)
n1 = str(input("primeiro produto: "))
n3 = str(input("segundo produto: "))
n2 = str(input("terceiro produto: "))
lista = [n1, n2, n3]
e = choice(lista)
print("=" * 40)
print("produto escolhido: {}".format(e))
print("=" * 40)
