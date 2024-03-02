from datetime import date
from time import sleep
ano = int(input("Digite o ano, para a analisar o ano atual 0:  "))
if ano == 0:
    ano = date.today().year
print("ANALISANDO O ANO...")
sleep(3)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto!".format(ano))
    print("=" * 30)
else:
    print("O ano de {} não é bissexto!".format(ano))
    print("=" * 30)
