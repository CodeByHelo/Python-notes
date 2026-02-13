num = int(input("Digite um número: "))
div = 0
for c in range (1, num + 1):
    if num % c == 0:
        print(f"\033[32m{c}\033[m", end = " -> ")
        div += 1
    else:
        print(f"\033[31m{c}\033[m", end = " -> ")
print("ACABOU!")
print(f"O núméro foi divisível {div} vezes")
if div == 2:
    print("E por isso ele É PRIMO")
else:
    print("E por isso ele NÃO é primo:")
