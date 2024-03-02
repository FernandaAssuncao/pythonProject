n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Foram digitados {} numeros PARES!!!".format(par))
print("Foram digitados {} numeros IMPARES!!!".format(impar))
