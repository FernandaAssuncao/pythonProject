n = list()
while True:
    nu = int(input("Digite um valor: "))
    if nu not in n:
        n.append(nu)
        print("Valor adicionado com sucesso!!!")
    else:
        print("Valor não foi adicionado!!!")
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? SIM[S] NÃO[N] ")).strip().upper()
    if resp == "N":
        break
print("=" * 35)
n.sort()
print(f"Lista de numeros digitados em ordem crecente: {n}")
