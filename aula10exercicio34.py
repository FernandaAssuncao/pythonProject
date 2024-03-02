from time import sleep
salario = float(input("Qual é o seu salário? R$"))
print("\033[1:36mANALISANDO O AUMENTO...\033[m")
print("-" * 25)
sleep(3)
if salario > 1250.00:
    aumento = salario * 10 / 100
    print("Seu salário com 10% de aumento: R${:.2f}".format(salario + aumento))
    print("=" * 42)
else:
    aumento = salario * 15 / 100
    print("Seu salário com 15% de aumento: R${:.2f}".format(salario + aumento))
    print("=" * 42)
