numero = int(input("Digite um numero: "))
divisor = 0
for c in range(1, numero+1):
    if numero % c == 0:
        divisor += 1
        print("\033[1:33m{}\033[m".format(c), end='->')
    else:
        print("\033[1:31m{}\033[m".format(c), end='->')
print("\nO valor {} é divisivel por \033[1:31m{}\033[m numeros!!!!".format(numero, divisor))
if divisor > 2:
    print("O valor digitado \033[1:36mNÃO É PRIMO!!!\033[m")
else:
    print("O valor digitado \033[1:36mÉ PRIMO!!!!\033[m")
