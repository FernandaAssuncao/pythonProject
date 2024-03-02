from math import pow
peso = float(input("Qual seu peso: "))
altura = float(input("Qual sua altura: "))
imc = peso / pow(altura, 2)
print("=" * 20)
print("Seu IMC: \033[36m{:.1f}\033[m".format(imc))
print("=" * 20)
print(" \033[1:35mSUA FAIXA É ...\033[m")
print("=" * 20)
if imc <= 18.5:
    print("ABAIXO DO PESO,\033[1:31mFIQUE ATENTO(a)!!!")
elif imc > 18.5 and imc <= 25.0:
    print("PESO IDEAL!!!")
elif imc > 25.0 and imc <= 30.0:
     print("SOBREPESO!!!")
elif imc > 30.0 and imc <= 40.0:
    print("OBESIDADE,\033[1:31mFIQUE ATENTO(a)!!!")
elif imc > 40:
    print("OBESIDADE MÓRBIDA,\033[1:31mTOME MUITO CUIDADO!!!")
