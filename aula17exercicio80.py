numeros = list()
for c in range(0, 5):
    nu = int(input("Digite um numero: "))
    if c == 0 or nu > numeros[len(numeros) - 1]:
        numeros.append(nu)
    else:
        pos = 0
        while pos < len(numeros):
            if nu <= numeros[pos]:
                numeros.insert(pos, nu)
                break
            pos += 1
print(f"Os valores em ordem são: {numeros}")
