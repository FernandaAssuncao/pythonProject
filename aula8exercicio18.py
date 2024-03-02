import math
a = float(input("digite o angulo: "))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print("o cosseno vale: {:.2f} \no seno vale: {:.2f} \no tagente vale: {:.2f}".format(c, s, t))
