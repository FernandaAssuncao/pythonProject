print("============ \033[1:35m10 PRIMEIROS TERMOS DE PA\033[m ============")
primeiro = int(input("Primeiro termo: "))
segundo = int(input("Razão: "))
decimo = primeiro + (10 - 1) * segundo
for c in range(primeiro, decimo + segundo, segundo):
    print("{}".format(c))
print("\033[1:31mFIM...\033[m")
