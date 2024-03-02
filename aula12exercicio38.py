numero = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))
if numero > numero2:
    print("\033[36m{}\033[m o primeiro valor digitado é maior!!!".format(numero))
    print("=" * 39)
elif numero2 > numero:
    print("\033[36m{}\033[m o segundo valor digitado é maior!!!".format(numero2))
    print("=" * 39)
elif numero == numero2:
    print("Os dois valores são \033[36miguais!!!\033[m")
    print("=" * 30)
