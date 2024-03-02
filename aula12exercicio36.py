valor = float(input("Qual valor da casa: "))
salario = float(input("Qual seu salario: "))
presti = int(input("Em quantos anos voce vai parcelar: "))
trinta = salario * 30 / 100
prestacao = valor / (presti * 12)
if trinta >= prestacao:
    print("Imprestimo comcedido!!!")
    print("Prestação: \033[1:35mR${:.3f}\033[m".format(prestacao))
    print("\033[1:36m=\033[m" * 20)
elif trinta < prestacao:
    print("Imprestimo negado!!!")
    print("\033[36m=\033[m" * 20)
