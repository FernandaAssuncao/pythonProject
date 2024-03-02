numero = int(input("Digite um valor: "))
c = 1
r = 1
while c != numero + 1:
    r = r * c
    c += 1
print("O falorial de {} é {}!!!".format(numero, r))
