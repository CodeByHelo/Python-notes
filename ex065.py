c = 1
num = int(input("Digite um número: "))
resp = str(input("Quer continuar? "))
maior = menor = soma = num
while resp.upper() == "S":
    num = int(input("Digite um número: "))
    soma += num
    c += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    resp = str(input("Quer continuar? "))
media = soma / c
print(f"Você digitou {c} valores e a média foi {media:.1f}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}.")