primeiro = int(input("Primeiro termo: "))
r = int(input("Razão: "))
termo = primeiro
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print("{} -> ".format(termo), end='')
        termo = termo + r
        cont += 1
    mais = int(input("Mais quantos termor? "))