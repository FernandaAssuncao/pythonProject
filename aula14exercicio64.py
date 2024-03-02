print("========== \033[1:31mANALISADOR DE NUMEROS!!!\033[m =============")
print("\033[1:34mOBS: DIGITE 999 PARA PARAR.\033[m")
tot = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input("Digite um valor: "))
    if numero != 999:
        soma += numero
        tot += 1
print("A soma entre todos os valores digitados é \033[1:35m{}!!!\033[m".format(soma))
print("Foram digitados \033[1:36m{}\033[m valores!!!".format(tot))
