from math import sqrt
from time import sleep
numero = int(input("Digite um numero: "))
raiz = sqrt(numero)
print("\033[1:35mANALISANDO O VALOR\033[m...")
sleep(3)
print("A raiz quadrada de {} é {:.2f}".format(numero, raiz))
print("=" * 30)
if raiz % 2 == 0:
    print("A raiz de {} é \033[1:32mPAR\033[m!!".format(numero))
    print("-" * 25)
else:
    print("A raiz de {} é \033[1:32mIMPAR\033[m!!".format(numero))
    print("-" * 25)
