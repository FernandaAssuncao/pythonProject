sexo = str(input("Imforme seu sexo [m/f]? ")).strip().lower()[0]
if sexo == "f" or sexo == "m":
    print("Sexo salvo com secesso!!!")
else:
    while sexo not in "fm":
        sexo = str(input("INVALIDO!!!,QUAL SEU SEXO [f/m]? ")).strip().lower()[0]
print("{} salvo com sucesso!!!".format(sexo))
