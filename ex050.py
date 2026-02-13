# Digite 6 números e somar os que forem PAR.
somap = 0
for c in range(1,7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        somap += num
print(f"A soma dos números pares digitados = {somap}")

