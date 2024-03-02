print("\033[1:32m===============\033[m \033[1:34mESCOLA URUBU\033[m \033[1:32m===============\033[m")
cont = melhor = soma = 0
nom = " "
while cont != 4:
    nome = str(input("Nome: "))
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    soma = (n1 + n2) / 2
    print(f"A MEDIA DE \033[1:36m{nome}\033[m: \033[1:36m{soma:.1f}\033[m")
    print("\033[1:35m=\033[m" * 35)
    cont += 1
    if soma > melhor:
        melhor = soma
        nom = nome
print(f"O melhor aluno foi \033[1:31m{nom}\033[m com a media \033[1:31m{melhor:.1f}!!!\033[m")
