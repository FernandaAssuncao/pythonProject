print("================== \033[1:31mBANCO FERNANDAS\033[m ======================")
valor = int(input("Qual o valor do saque? R$"))
si = valor // 50
valor %= 50
vi = valor // 20
valor %= 20
des = valor // 10
valor %= 10
um = valor // 1
print(f"NOTAS DE R$50: {si}")
print(f"NOTAS DE R$20: {vi}")
print(f"NOTAS DE R$10: {des}")
print(f"NOTAS DE R$1: {um}")
