from math import pow
from time import sleep
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / pow(altura, 2)
print("\033[1:34mANALISANDO...\033[m")
sleep(3)
print("Seu imc: \033[36m{:.2f}\033[m".format(imc))
print("=" * 20)
print("\033[1:35mFAIXAS DE IMC!!!\033[m")
print("=" * 20)
if imc < 18.5:
    print("Você está abaixo do peso!!!")
    print("=" * 30)
if imc > 18.6 and imc < 24.9:
    print("Você está saudavel!!")
    print("=" * 20)
if imc > 25.0 and imc < 29.9:
    print("Peso em excesso!!")
    print("=" * 20)
if imc > 30.0 and imc < 34.9:
    print("Você está em Obesidade de GRAU I")
    print("=" * 30)
if imc > 35.0 and imc < 39.9:
    print("Você está em Obesidade de GRAU II[SEVERA]")
    print("=" * 40)
if imc > 40:
    print("Você está em Obesidade de GRAU III[MÓRBIDA]")
    print("=" * 40)
