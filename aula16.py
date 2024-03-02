lanche = ("Hamburgue", "Suco", "Pizza", "Pudim", "Batata Frita")

print(sorted(lanche))

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")

print("=" * 30)

for comida in lanche:
    print(f"Eu vou comer {comida}")

print("COMI PÁ CARAMBA")

del(lanche)
print(lanche)
