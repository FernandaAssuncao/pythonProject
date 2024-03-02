valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? SIM[S] NÃO[N] ")).strip().upper()
    if resp == "N":
        break
print("=" * 51)
print(f"LISTA DE NUMEROS DIGITADOS: \033[1:31m{valores}\033[m")
print(f"Na lista foram digitados \033[1:35m{len(valores)}\033[m numeros!!!")
valores.sort(reverse=True)
print(f"Lista em forma decrescente: \033[1:34m{valores}\033[m")
if 5 in valores:
    print("O valor \033[1:36m5 está\033[m na lista!!!")
else:
    print("O valor \033[1:36m5 não\033[m está na lista!!!")
