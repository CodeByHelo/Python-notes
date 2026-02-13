soma = 0
mulher = 0
velho = ""
maior = 0
for c in range(1,5):
    print(f"----- {c}ª PESSOA -----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    soma += idade
    if sexo == "M":
        if idade > maior:
            maior = idade
            velho = nome
    else:
        if idade < 20:
            mulher += 1
media = soma / c
print(f"A média de idade do grupo é de {media} anos")
print(f"O homem mais velho tem {maior} anos e se chama {velho}")
print(f"Ao todo são {mulher} mulheres com menos de 20 anos")

