from time import sleep
distancia = float(input("Digite a distancia da viagem km/h: "))
print("ANALISANDO...")
sleep(4)
if distancia <= 200.0:
    print("=" * 31)
    print("A passagem custara: R${:.2f}".format(distancia * 0.50))
    print("=" * 31)
else:
    print("=" * 31)
    print("A sua passagem custara: R${:.2f}".format(distancia * 0.45))
    print("=" * 31)
