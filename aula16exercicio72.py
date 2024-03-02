contagem = ("Zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onse", "dose", "treze", "quatorze", "quinse", "dezesseis", "tesecete", "tesoito", "desenove", "vinte")
resp = "S"
while True:
    numero = -1
    while numero < 0 or numero > 20:
        numero = int(input("Digite um numero entre 0 e 20: "))
    print(f"O valor digitado foi \033[1:31m{contagem[numero]}!!!\033[m")
    resp = str(input("Quer continuar? SIM[S] NÃO[N]")).strip().upper()[0]
    if resp == "N":
        break
