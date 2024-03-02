frase = str(input("Digite um frase: ")).upper().strip()
frasee = frase.split()
junto = ''.join(frasee)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("A frase digitada é um PALINDROMO!!!")
else:
    print("A frase não é um PALINDROMO!!!")
