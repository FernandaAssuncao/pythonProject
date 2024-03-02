valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
for v, c in enumerate(valores):
    print(f"\n{c} está na posição {v}", end='')
print("\nFim da lista!!!")
