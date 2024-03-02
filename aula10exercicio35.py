n1 = float(input("Digite a primeira reta: "))
n2 = float(input("Digite a segunda reta: "))
n3 = float(input("Digite a terceira reta: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print("As retas acima \033[1:32mFORMAN\033[m um triângulo!!")
    print("=" * 40)
else:
    print("As retas acima \033[1:32mNÃO FORMAN\033[m um triângulo!!")
    print("=" * 40)
