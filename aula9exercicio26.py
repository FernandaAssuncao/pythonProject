nome = str(input("digite uma frase: ")).lower().strip()
print("A letra 'A' aparece {} vezes!!".format(nome.count("a")))
print("A primeira letra A aparace na posição: {}".format(nome.find("a") + 1))
print("A ultima letra A apareceu na posição: {}".format(nome.rfind("a") + 1))
