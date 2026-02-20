
maior18 = homem = mulher = 0
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)

    idade = int(input("Idade: "))
    if idade > 18:
        maior18 += 1

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    if sexo == "F" and idade < 20:
        mulher += 1
    elif sexo == "M":
        homem +=1

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if resp == 'N':
        break
print(f"O total de pessoas com mais de 18 anos: {maior18}")
print(f"Ao todos temos {homem} homens cadastrados.")
print(f"E temos {mulher} mulheres com menos de 20 anos.")
