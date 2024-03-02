print("=================== \033[1:33mANALISADOR DE NUMEROS 1.0\033[m ======================")
print("\033[1:34mIMPORTANTE: digite 999 para imterromper a digitação...\033[m")
soma = tot = 0
while True:
    n = int(input("Digite um numero: "))
    if n != 999:
        soma += n
        tot += 1
    elif n == 999:
        break
print(f"Foram digitados \033[1:35m{tot} numeros\033[m e a soma entre eles é \033[1:31m{soma}\033[m.")
