valores = []
impar = []
pares = []
while True:
    n = int(input("Digite um valor: "))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impar.append(n)
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? SIM[S] NÃO[N] ")).strip().upper()
    if resp == "N":
        break
print("=" * 45)
print(f"LISTA DOS VALORES DIGITADOS: \033[1:35m{valores}\033[m")
print(f"LISTA SÓ COM NUMEROS PARES: \033[1:31m{pares}\033[m")
print(f"LISTA SÓ COM NUMEROS IMPARES: \033[1:34m{impar}\033[m ")
