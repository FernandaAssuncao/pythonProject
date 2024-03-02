lanche = ("hamburguer", "suco", "pizza", "pudim", "batata frita")
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")

for comida in lanche:
    print(f"Eu vou comer {comida}")

for por, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posiçao {por}")

print("NOSSA,comi muito!!!")
