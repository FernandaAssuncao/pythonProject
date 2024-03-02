numero = int(input("Digite um numero: "))
print('''Escolhas uma das opções abaixo: 
[1] para BINARIO 
[2] para OCTAL
[3] para HEXADECIMAL''')
opcao = int(input("Qual a sua opção? "))
if opcao == 1:
    print("{} em BINARIO: {}".format(numero, bin(numero)[2:]))
elif opcao == 2:
    print("{} em OCTAL: {}".format(numero, oct(numero)[2:]))
elif opcao == 3:
    print("{} comvertido em HEXADECIMAL: {}".format(numero, hex(numero)[2:]))
