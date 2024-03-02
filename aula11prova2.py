from time import sleep
print("Comvertor de \033[1:33mmetros\033[m para \033[1:33mquilometros!!!\033[m")
print("=" * 40)
metros = float(input("Digite um valor em metros: "))
km = metros / 1000
print("\033[1:36mFAZENDO A COMVERÇÃO...\033[m")
print("\033[1:31m=\033[m" * 26)
sleep(3)
print("km/h: \033[1:35m{}\033[m".format(km))
print("\033[1:31m=\033[m" * 16)
