print("============= \033[1:31mLOJAS FERNANDAS\033[m ==============")
produto = float(input('Qual o Preço total dos produtos: '))
forma = int(input("""Qual forma de pagamento: 
\033[1:35m[1] dinherio ou cheque
[2] avista no quartão
[3] parcelado em 2 vezes no quartão 
[4] mais de 3 vezes no quartão\033[m 
 """))
print("\033[36m=\033[m" * 50)
if forma == 1:
    desconto = produto * 10 / 100
    print("O preço dos produtos tera 10% de desconto então ficara: R${:.2f}".format(produto - desconto))
elif forma == 2:
    desconto = produto * 5 / 100
    print("O preço dos produtos tera 5% de desconto então ficara: R${:.2f}".format(produto - desconto))
elif forma == 3:
    print("Você devera pagar duas parcelas de: R${:.2f}".format(produto / 2))
if forma == 4:
    vezes = int(input("Em quantas vezes você vai parcelar? "))
    total = produto + (produto * 20 / 100)
    print("Você devera pagar {} parcelas de {:.2f} com juros!!!".format(vezes, total / vezes))
elif forma >= 5:
    print("\033[1:31mOpção invalida, tente novamente!!\033[m")
