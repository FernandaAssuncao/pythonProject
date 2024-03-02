from time import sleep
from math import pow
numero = int(input("Digite um numero: "))
numero1 = int(input("Digite outro numero: "))
resultado = pow(numero, 2)
resultado2 = pow(numero1, 2)
print("\033[35mANALISANDO...AGUADE...\033[m")
print("=" * 20)
sleep(3)
print("O resultado de {} elevado a 2 é {}".format(numero, resultado))
print("O resultado de {} elevado a 2 é {}".format(numero1, resultado2))
if resultado > resultado2:
    print("\033[1:36m=\033[m" * 34)
    print("O maior resultado foi o primeiro numero digitado: {}!".format(resultado))
else:
    print("\033[1:36m=\033[m" * 34)
    print("O maior resultado foi o segundo numero digitado: {}!".format(resultado2))
