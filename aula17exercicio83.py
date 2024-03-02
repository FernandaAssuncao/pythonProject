espre = str(input("Digite uma espressão numerica: "))
pilha = []
for simb in espre:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Expressão valida")
else:
    print("Expressão invalida!")

