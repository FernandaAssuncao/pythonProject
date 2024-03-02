from random import randint
print("================ \033[1:34mPAR OU IMPAR COM O COMPUTADOR!!!\033[m ==================")
tot = soma = 0
while True:
    computador = randint(0, 10)
    usuario = int(input("Digite um numero: "))
    pi = str(input("PAR[P] OU IMPAR[I]: ")).upper().strip()
    soma = computador + usuario
    if pi == "P":
        print("O computador ficou com impar!!!")
        if soma % 2 == 0:
            print("\033[1:35mO vencedor foi o usuario!!!\033[m")
            print(f"O computador escolheu o numero \033[1:36m{computador}!!!\033[m,ou seja a soma é {soma}.")
            tot += 1
        elif soma % 2 == 1:
            print("\033[1:35mO vencedor foi o computador!!!\033[m")
            print(f"O computador escolheu o numero \033[1:36m{computador}!!!\033[m,ou seja a soma é {soma}.")
            break
    if pi == "I":
        print("O computador ficou com PAR!!!")
        if soma % 2 == 1:
            print("\033[1:35mO vencedor foi o usuario!!!\033[m")
            print(f"O computador escolheu o numero \033[1:36m{computador}!!!\033[m,ou seja a soma é {soma}.")
            tot += 1
        elif soma % 2 == 0:
            print("\033[1:35mO vencedor foi o computador!!!\033[m")
            print(f"O computador escolheu o numero \033[1:36m{computador}!!!\033[m,ou seja a soma é {soma}.")
            break
print("\033[1:36m=\033[m" * 29)
print("\033[1:31mFIM DE JOGO!!!!\033[m")
print(f"Você obteve \033[1:31m{tot} vitorias!!!\033[m")
print("\033[1:36m=\033[m" * 29)
