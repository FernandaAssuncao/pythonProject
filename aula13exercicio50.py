s = 0
for c in range(1, 7):
    valor = int(input("Digite o {}º valor: ".format(c)))
    if valor % 2 == 0:
        s += valor
print("=" * 40)
print("A soma de todos valores \033[1:36mPARES\033[m é \033[1:31m{}!!!\033[m".format(s))
print("=" * 40)
