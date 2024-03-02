from random import randint
t = 0
computador = randint(0, 10)
print("============== \033[1:31mVOCÊ COMSEGUE VENCER O COMPUTADOR?\033[m ================")
print("""        \033[1:34m regras
[1] O COMPUTADOR VAI PENSAR EM UM VALOR DE 0 A 10
[2]ENTÃO DEPOIS TENTE ADIVINHAR DIGITANDO
UM VALOR DE 1 A 10!!!\033[m""")
usuario = 20
while usuario != computador:
    usuario = int(input("Em qual valor eu pensei? "))
    print("\033[1:35m=\033[m" * 25)
    t += 1
print("\033[1:33mParabens voce me venceu\033[m mais foram necessarias \033[1:36m{}\033[m palpites!!!".format(t))
print("Eu escolhi o numero \033[1:36m{}\033[m!!!".format(computador))
