from time import sleep
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print("\033[1:35mANALISANDO...\033[m")
print("=" * 20)
sleep(3)
print("Medía: \033[1:35m{:.1f}\033[m".format(media))
print("=" * 20)
if media < 5.0:
    print("Aluno \033[1:31mReprovado!!\033[m")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em \033[1:31mRecuperação!!!\033[m")
elif media >= 7.0:
    print("Aluno \033[1:31mAprovado!!!\033[m")
