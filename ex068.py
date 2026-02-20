from random import randint

print("=-" * 15)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-" * 15)

win = 0

while True:
    comp = randint(1, 10)
    num = int(input("Digite um valor: "))
    soma = num  + comp
    escolha = " "
    while escolha not in 'IP':
        escolha = str(input("Par ou ímpar? [P/I] ")).upper()[0]
    print("-"*30)
    print(f"Você jogou {num} e o computador {comp}. Total de {soma} DEU ", end =" ")
    print("PAR" if soma % 2 == 0 else "ÍMPAR")
    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = 'I'
    if resultado == escolha:
        print("Você ganhou. Vamos jogar novamente...")
        win += 1
    else:
        print(f"GAME OVER! Você venceu {win} vezes")
        break
    print("-" * 30)
