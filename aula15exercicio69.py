print("=============== \033[1:33mCADRASTRO DE PESSOAS!!!\033[m =================")
tot = hm = ml = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [F]FEMINO [M]masculino: ")).strip().upper()
    resposta = str(input("Quer continuar? SIM[S] NÃO[N]: ")).strip().upper()
    print("\033[1:35m=\033[m" * 35)
    if idade > 18:
       tot += 1
    if sexo == "M":
        hm += 1
    if sexo == "F" and idade < 20:
        ml += 1
    if resposta == "N":
        break
print(f"Foram cadrastradas \033[1:31m{tot}\033[m pessoas acima de 18 anos!!!")
print(f"Foram cadrastrados \033[1:34m{hm}\033[m homens!!!")
print(f"Foram cadratradas \033[1:36m{ml}\033[m mulheres menores de 20 anos!!!")
print("\033[1:35m=\033[m" * 45)
