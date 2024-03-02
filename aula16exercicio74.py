from random import randint
print("============= \033[1:34mSORTEADOR DE VALORES!!!\033[m ==============")
n1 = randint(0, 10000)
n2 = randint(0, 10000)
n3 = randint(0, 10000)
n4 = randint(0, 10000)
n5 = randint(0, 10000)
numeros = (n1, n2, n3, n4, n5)
maior = 0
menor = numeros[0]
print("Os valores sorteados foram: ")
for c in range(0, len(numeros)):
    print(f"\033[1:36m{numeros[c]}\033[m ", end='')
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print(f"\nO maior valor foi: \033[1:35m{maior}\033[m")
print(f"O menor valor foi: \033[1:31m{menor}\033[m")
