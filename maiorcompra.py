print("================= \033[1:34mLOJAS AMERICANAS\033[m =================")
maior = total = 0
resp = "S"
while True:
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    resp = str(input("Quer continuar comprando? SIM[S] NÃO[N] ")).strip().upper()
    print("\033[1:35m=\033[m" * 39)
    total += preco
    if preco > maior:
        maior = preco
    if resp == "N":
        tot = int(input("Em quantas vezes você vai pagar? "))
        break
print("\033[1:35m=\033[m" * 39)
print(f"TOTAL DA COMPRA: R$\033[1:31m{total:.2f}\033[m")
if tot > 1:
    print(f"Total parcelado em \033[1:31m{tot}\033[m vezes: R$\033[1:31m{total / tot:.2f}\033[m")
