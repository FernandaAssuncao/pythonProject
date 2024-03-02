nome = str(input("Digite seu nome: ")).strip().upper()
idade = int(input("Digite sua idade: "))
if nome == "MARIA":
    print("NOSSA, você tem um nome comum!!!")
    print("-" * 30)
else:
    print("Que nome bonito!!!")
    print("-" * 20)
if idade > 18:
    print("Você já pode retirar sua quarteira de motorista!!!")
    print("-" * 60)
else:
    print("Você ainda não pode retirar a sua quarteira de motorista!!!")
    print("-" * 60)
