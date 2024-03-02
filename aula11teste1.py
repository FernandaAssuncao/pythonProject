from math import pow
numero = int(input("Digite um numero: "))
resultado = pow(numero, 3)
print("\033[1:34m=\033[m" * 35)
print("\033[1:30m0 numero {} elevado ao cubo é {}\033[m".format(numero, resultado))
print("\033[1:34m=\033[m" * 35)
if resultado % 2 == 0:
    print("O resultado de {} elevado ao cubo é um numero \033[1:36mPAR\033[m!!!".format(numero))
else:
    print("O resultado de {} elevado ao cubo é um numero \033[1:35mIMPAR\033[m!!!".format(numero))
