nn = int(input("digite um valor: "))
u = nn // 1 % 10
d = nn // 10 % 10
c = nn // 100 % 10
m = nn // 1000 % 10
print("O numero digitado separado por casa: {}".format(nn))
print("unidade: {}".format(u))
print("dezena: {}".format(d))
print("centena: {}".format(c))
print("milhar: {}".format(m))
