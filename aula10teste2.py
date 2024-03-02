from random import choice
from time import sleep
print("\033[31m-=\033[m" * 30)
print("         \033[1:36mVOCÊ COMCEGUE VENCER O COMPUTADOR?\033[m       ")
print("\033[31m-=\033[m" * 30)
lista = ["abelha", "borboleta", "largata", "joaninha"]
computador = choice(lista)
usuario = str(input("Escolha entre esses tres incetos: abelha,borboleta,largata ou joaninha: "))
print("PROCESSANDO...")
sleep(3)
if usuario == computador:
    print("Parabens voce venceu o computador!!!")
    print("=" * 35)
else:
    print("O computador venceu!!!")
    print("=" * 30)
print("O inceto escolhido pelo computador foi: {}".format(computador))
print("=" * 50)
