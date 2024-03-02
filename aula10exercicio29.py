v = float(input("Digite a velocidade do carro: km "))
if v > 80.0:
    print("Voce está acima do limite de 80km/h, voce foi multado!!!")
    multa = (v - 80) * 7
    print("A multa foi no valor de: R${:.2f}".format(multa))
    print("=" * 40)
else:
    print("Você está dentro do limite!!")
    print("Continue assim!!!")
    print("=" * 29)
