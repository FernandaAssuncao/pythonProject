from time import sleep
valor = int(input("Digite um valor: "))
print("PROCESSANDO...")
sleep(4)
if valor % 2 == 0:
    print("=" * 25)
    print("O valor {} é PAR!!".format(valor))
    print("=" * 25)
else:
    print("=" * 25)
    print("O valor {} é IMPAR!!".format(valor))
    print("=" * 25)
