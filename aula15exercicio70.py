print("============= \033[1:34mLOJA TUDO BARATINHO _._._\033[m =============")
valor = tot = 0
nm = ""
menor = 9999
while True:
    nome = str(input("Nome do Produto: "))
    produto = float(input("Preço: R$"))
    valor += produto
    if produto > 1000.00:
        tot += 1
    if produto < menor:
        nm = nome
        menor = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar comprando SIM[S] NÃO[N]: ")).strip().upper()
    if resp == "N":
        break
print("\033[1:36m=" * 49)
print("\033[1:35mCOMPRA FINALISADA COM SUCESSO!!\033[m")
print(f"Valor final : \033[1:31mR${valor:.2f}\033[m")
print(f"\033[1:31m{tot}\033[m produtos custaram mais de R$1000,00!!!")
print(f"O produto mais barato foi \033[1:31m{nm}\033[m custando \033[1:31m{menor}\033[m")
print("\033[1:36m=\033[m" * 49)
