from random import randint
from time import sleep
nome = str(input("Digite o nome que voce quer: "))
print("=" * 20)
print(" \033[36mCUMPUTADOR\033[m \033[30mVS\033[m \033[36m{}\033[m ".format(nome.upper()))
print("=" * 20)
n = randint(0, 5)
nn = int(input("Digite um valor de 0 a 5: "))
print("Processando...")
sleep(3)
print("=" * 13)
if nn == n:
    print("{} venceu, parabens!!!".format(nome.upper()))
    print("-" * 30)
else:
    print("O computador venceu!!!")
    print("-" * 20)
print("O valor digitado pelo cumputador foi: {}".format(n))
print("=" * 40)
