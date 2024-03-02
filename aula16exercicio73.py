times = ("Palmeiras", "Santos", "Vasco da Gama", "Grêmio", "Flamengo", "Corinthias", "Internacional", "Cruzeiro", "São Paulo", "Atlético Mineiro", "Botafogo", "Fluminence", "Coritiba", "Bahia", "Goiás", "Guarani", "Sport", "Portuguesa", "Atlético Paranience", "Vitória")
print(f"Os primeiros 20 colocados do Brasilerão são: {times}")
print(f"Os 5 PRIMEIROS Colocados  são: {times[0:5]}")
print(f"Os umtimos 4 colocados são: {times[16:]}")
print(f"NOME dos times em ordem alfebetica: {sorted(times)}")
posicao = times.count('chapecoence')
if posicao == 0:
    print("O time CHAPECOENCE NÃO está nos 20 primeios colocados,ou seja,está na posição 0!!!")
else:
    print(f"O time CHAPECOENCE está na posição {posicao}")
