print("=========== \033[1:31mANALISADOR DE PESSOAS!!\033[m ==========")
hm = ""
maior = 0
tot = 0
medi = 0
for c in range(1, 5):
    nome = str(input("Qual o nome da {}º pessoa? ".format(c))).strip()
    idade = int(input("Qual a idade da {}º pessoa? ".format(c)))
    sexo = str(input("Qual seu sexo [f] feminino [m] masculino: ")).lower().strip()
    print("\033[1:31m=\033[m" * 45)
    medi += idade
    if sexo == "m" and idade > maior:
        maior = idade
        hm = nome
    elif sexo == "f" and idade < 20:
        tot += 1
print("MEDIA DE IDADES: \033[1:33m{}\033[m".format(medi / 4))
print("O homen mais velho é \033[1:35m{}\033[m com \033[1:35m{}\033[m anos!!!".format(hm, maior))
print("Existem \033[1:36m{}\033[m mulheres menores de 20 anos!!!".format(tot))
print("\033[1:31m=\033[m" * 45)
