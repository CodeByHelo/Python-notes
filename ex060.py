num = int(input("Digite um número para calcular o fatorial: "))
total = 1
print(f"Calculando {num}! -> ",end = "")
while num >= 1:
    print(num, end= "")
    print(" x " if num > 1 else  " = ", end ="")
    total *= num
    num -= 1
print(total)
