c = soma = num = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        soma += num
        c += 1
print(f"Você digitou {c} números e a soma entre eles foi {soma}")