from datetime import date
print("=" * 20)
print("\033[1:35mCATEGORIA DE ATLETAS\033[m ")
print("=" * 20)
ano = int(input("Em que ano você naceu? "))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print("Você é da categoria MIRIN!!!")
elif idade > 9 and idade <= 14:
    print("Você é da categoria INFANTIL!!!")
elif idade > 14 and idade <= 19:
    print("Você é da categoria JUNIR!!!")
elif idade > 19 and idade <=25:
    print("Você é da categoria SÊNIR!!!")
elif idade > 25:
    print("Você é da categoria master!!!")
