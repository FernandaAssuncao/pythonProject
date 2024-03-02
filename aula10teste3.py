n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
print("-" * 30)
media = (n1 + n2) / 2
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
print("-" * 30)
media1 = (n3 + n4) / 2
n5 = float(input("Digite a quinta nota: "))
n6 = float(input("Digite a sexta nota: "))
media2 = (n5 + n6) / 2
print("-" * 30)
print("A media do  primeiro semestre: {:.1f}".format(media))
print("A media do segundo semestre: {:.1f}".format(media1))
print("A media do terceiro semestre: {:.1f}".format(media2))
print("=" * 40)
if media > 8.5 and media1 > 8.5 and media2 > 8.5:
    print("O aluno \033[36mganhou medelha\033[m!!!")
    print("=" * 30)
else:
    print("O aluno \033[34mnão ganhou medelha\033[m!!!")
    print("=" * 30)
