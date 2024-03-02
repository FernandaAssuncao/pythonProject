nome = str(input("Digite seu nome: "))
if nome == "fernanda":
    print("Que nome bonito!!!")
elif nome == "pedro" or nome == "maria" or nome == "joão":
    print("Seu nome é bem popular no Brasil..")
else:
    print("Que nome normal!!!")
print("Tenha um bom dia {}!!!".format(nome))
