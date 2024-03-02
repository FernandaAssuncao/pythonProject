r = "s"
media = 0
maior = 0
menor = 9999
tot = 0
while r != "n":
    numero = int(input("Digite um valor: "))
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    tot += 1
    media += numero
    r = str(input("Quer continuar? SIM[S] NÃO[N]: ")).strip().lower()
print("=" * 44)
print("\033[1:31mMAIOR VALOR: {}\033[m".format(maior))
print("\033[1:35mMENOR VALOR: {}\033[m".format(menor))
print("A \033[1:36mMEDIA\033[m ENTRE TODOS OS VALORES É: \033[1:36m{:.2f}\033[m".format(media / tot))
print("=" * 44)
