numero = int(input("Digite um valor: "))
print("\033[1:30m=\033[m" * 20)
print("\033[1:35mTABOADA DO\033[m \033[1:31m{}\033[m".format(numero))
print("\033[1:30m=\033[m" * 20)
for c in range(1, 11):
    r = c * numero
    print("{} * {} = \033[1:36m{}\033[m".format(numero, c, r))
