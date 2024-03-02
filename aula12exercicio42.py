n1 = float(input("Digite a primeira reta: "))
n2 = float(input("Digite a segunda reta: "))
n3 = float(input("Digite a terceira reta: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("As retas acima forman um Triangulo!!!")
    if n1 == n2 == n3:
        print("EQUILATERO!!!")
    elif n1 != n2 != n3 != n1:
        print("Escaleno!!!")
    else:
        print("ISOCILIS!!!")
else:
    print("As retas acima não formam um triangulo!!!")
