from random import choice
lista = ["pedra", "papel", "tesoura"]
computador = choice(lista)
print("\033[1:30m===========\033[m \033[1:31mJoquempó\033[m \033[1:30m===========\033[m")
jogador = str(input("Pedra,papel ou tesoura: "))
print("\033[1:36m=\033[m" * 30)
if computador == "pedra" and jogador == "papel":
    print("O vencedor é o jogador")
elif computador == "pedra" and jogador == "tesoura":
    print("O vencedor é o computador")
elif computador == "pedra" and jogador == "pedra":
    print("Impate!!!")
elif computador == "papel" and jogador == "papel":
    print("Impate!!!")
elif computador == "papel" and jogador == "tesoura":
    print("O jogador venceu!!!")
elif computador == "papel" and jogador == "pedra":
    print("O vencedor é o computador!!!")
elif computador == "tesoura" and jogador == "pedra":
    print("O vencedor é o jogador!!!")
elif computador == "tesoura" and jogador == "papel":
    print("O vencedor é o computador!!")
elif computador == "tesoura" and jogador == "tesoura":
    print("Impate!!!")
print("\033[1:36m=\033[m" * 30)
print("O computador escolheu \033[1:35m{}".format(computador))
