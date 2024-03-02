palavras = ("passaros", "agaporni", "capapcita", "mandarin")
for c in palavras:
    print(f"\nNa palavra {c} existem as vogais ", end='')
    for letra in c:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
