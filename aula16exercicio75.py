numeros = (int(input("Digite um valor: ")),
           int(input("Digite um valor: ")),
           int(input("Digite um valor: ")),
           int(input("Digite um valor: ")),)
print("\033[1:31m=\033[m" * 36)
print(f"Os valores digitados foram: {numeros}")
print(f"O valor 9 apareceu {numeros.count(9)} vezes!!")
if 3 in numeros:
    print(f"O primeiro valor 3 foi digitado na posição {numeros.index(3)}")
else:
    print("O valor 3 não foi digitado!!!")
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(f"{numeros[c]} ", end='')
print("são valores pares!! ")
