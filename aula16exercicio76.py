produtos = ("Pão", 5.98, "Leite", 10.99, "Açucar", 34.98, "Carne", 56.90)
print("============ \033[1:31mLISTAGEM DE PREÇOS!!!\033[m ============")
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f"{produtos[c]:.<30}", end='')
    else:
        print(f"R$ {produtos[c]:>5.2f}")
print("\033[1:31m=\033[m" * 48)
