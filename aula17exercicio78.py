numeros = list()
maior = 0
for c in range(0, 5):
    numeros.append(int(input("Digite um valor: ")))
menor = numeros[0]
for c in range(0, len(numeros)):
    if numeros[c] >= maior:
        maior = numeros[c]
    if numeros[c] <= menor:
        menor = numeros[c]
print(f"Os valores digitados foram {numeros}")
print(f"O maior valor foi {maior} na posição ", end='')
for c, v in enumerate(numeros):
    if v == maior:
        print(f"{c}....", end='')
print(f"\nO menor valor foi {menor} na posição ", end='')
for c, v in enumerate(numeros):
    if v == menor:
        print(f"{c}...", end='')
