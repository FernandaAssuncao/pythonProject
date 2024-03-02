from datetime import date
anoa = date.today().year
m = 0
n = 0
for c in range(1, 8):
    ano = int(input("Em que ano a {}º nasceu? ".format(c)))
    idade = anoa - ano
    if idade > 18:
        m += 1
    else:
        n += 1
print("Foram digitadas \033[1:35m{}\033[m pessoas acima da idade!!!".format(m))
print("Foram digitadas \033[1:31m{}\033[m pessoas menores de idade!!!".format(n))
