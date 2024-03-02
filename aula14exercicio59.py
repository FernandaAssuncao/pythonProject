r = 0
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
while r != 5:
    r = int(input("""\033[1:31mMENU
    [1] somar
    [2] multiplicar 
    [3] maior 
    [4] novos valores 
    [5] sair do menu \033[m
    Qual a sua opção: """))
    print("\033[1:36m=\033[m" * 20)
    if r == 1:
        print("\033[1:35mA soma entre {} e {} é {}!!\033[m".format(n1, n2, n1 + n2))
    elif r == 2:
        print("\033[1:34mA multiplicação entre {} e {} é {}!!\033[m".format(n1, n2, n1 * n2))
    if r == 3:
        if n1 > n2:
            print("\033[1:33mO {} é o MAIOR!!\033[m".format(n1))
        else:
            print("\033[1:33mO {} é o MAIOR!!\033[m".format(n2))
    if r == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
    if r > 5:
        print("Opção invalida!!!!")
print("\033[1:36mSAINDO...:(\033[m")
