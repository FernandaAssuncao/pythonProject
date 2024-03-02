print("=================== \033[1:31mTABOADAS DE VARIOS NUMEROS!!!\033[m ====================")
print("\033[1:34mOBS: DIGITE UM VALOR NEGATIVO QUANDO QUISER ENCERRAR O PROGAMA!!!\033[m")
c = 1
while True:
    n = int(input("Digite um valor para ver sua taboada: "))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} * {c} = \033[1:35m{n * c}\033[m")
        c += 1
print("\033[1:33mENCERRANDO...\nVOLTE SEMPRE!!!\033[m")
print("\033[1:36m=\033[m" * 20)
