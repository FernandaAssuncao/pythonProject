num = list(range(4, 9))
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(4, 6)
num.append(5)
if 9 in num:
    num.remove(9)
print(num)
print(f"Essa lista tem {len(num)} elementos")
