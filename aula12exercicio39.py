from datetime import date
print("=" * 45)
print(" \033[1:34mALISTAMENTO PARA O EXERCITO\033[m ")
print("=" * 45)
ano = int(input("Em que ano você naceu: "))
anoatual = date.today().year
idade = anoatual - ano
if idade < 18:
    print("=" * 45)
    print("Você ainda não pode se alistar!!!")
    print("Faltam \033[1:34m{}\033[m anos para que você possa se alistar!!".format(18 - idade))
elif idade == 18:
    print("=" * 45)
    print("Já está na hora de se alistar!!!")
elif idade > 18:
    print("=" * 45)
    print("Já passou da hora de se alistar!!!")
    print("Se passou \033[1:34m{}\033[m anos do tempo que você podia se alistar!!".format(idade - 18))
