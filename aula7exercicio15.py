km = float(input("Digite o km percorrido pelo carro: "))
d = int(input("Por quantos dias o carro foi usado: "))
t = d * 60
tt = km * 0.15
print("=" * 30)
print("Total do aluguel: R${:.2f}".format(t + tt))
print("=" * 30)
