import random

print("Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
computador = random.randint(0,10)
acertou = False
tent = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    tent += 1
    if jogador < computador:
        print("Mais...", end = " ")
    elif jogador > computador:
        print("Menos...", end = " ")
    if jogador == computador:
        acertou = True
        print(f"Acertou com {tent} tentativas. Parabéns!")

