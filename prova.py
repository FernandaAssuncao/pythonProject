print("================== \033[1:31mA TEMPERATURA DA CIDADE ESTÁ MUITO ALTA?\033[m ===================")
while True:
    cidade = str(input("Nome da cidade: ")).strip()
    temperatura = float(input("Temperatura: "))
    if temperatura >= 30.0:
        print(f"Na cidade  {cidade} está muito quente!!!")
    elif temperatura <= 10.0:
        print(f"Na cidade {cidade} está muito frio!!!")
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar?  SIM[S] NÃO[N] ")).strip().upper()
    if resp == "N":
        break
