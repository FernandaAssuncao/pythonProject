s = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        cont += 1
        s += c
print("A soma entre todos os {} \033[1:31mVALORES IMPARES\033[m e \033[1:35mMULTIPLOS DE 3\033[m É \033[36m{}".format(cont, s))
