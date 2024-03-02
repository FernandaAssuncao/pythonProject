p = float(input("preço do produto: "))
a = p * 10 / 100
c = p * 2 / 100
print("-" * 50)
print(" forma de pagar diferente um desconto diferente!!! ")
print("-" * 50)
print("Pagamento avista: {:.2f} reais".format(p - a))
print("pagamento no cartão: {:.2f} reais".format(p - c))
