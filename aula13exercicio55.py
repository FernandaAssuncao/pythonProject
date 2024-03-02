print("============== \033[1:34mQUEM TEM O MAIOR E MENOR PESO?\033[m ================")
maior = 0
menor = 100
for c in range(1, 6):
    peso = float(input("Qual o peso {}º peso? ".format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O \033[1:31mMAIOR\033[m peso foi \033[1:35m{}\033[m".format(maior))
print("O \033[1:36mMENOR\033[m peso foi \033[1:35m{}\033[m".format(menor))
