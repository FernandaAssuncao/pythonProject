from math import pow
from time import sleep
numero = int(input("Digite o Raio do circulo: "))
area = pow(numero, 2)
print("CALCULADNO...")
print("\033[1:35m=\033[m" * 16)
sleep(3)
print("Area do circulo: \033[1:31m{}\033[m".format(area))
