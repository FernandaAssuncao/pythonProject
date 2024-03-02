n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua medía é {:.1f}".format(m))
if m >= 6.0:
    print("Sua media foi ótima!!!")
else:
    print("Sua media não foi ótima!!! você precisa melhorar!!!")
