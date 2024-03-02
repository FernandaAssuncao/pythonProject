from math import sqrt
n = float(input("digite o primeiro cateto: "))
n2 = float(input("digite a segunda cateto: "))
t = (n**2) + (n2**2)
tt = sqrt(t)
print("A impotenusa do triangulo é: {:.2f}".format(tt))
