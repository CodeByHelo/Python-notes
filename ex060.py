num = int(input("Digite um número para calcular seu fatorial: " ))
c = num
fat = 1
while 1 <= c <= num:
    if c != 1:
        print(c, end = " x ")
        total = (num * (c - 1))
        fat *= total
        c -= 1
print(f"= {fat}")

