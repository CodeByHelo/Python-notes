import random
opções = ["Pedra", "Papel", "Tesoura"]
computador = random.choices(opções)
print("OPÇÕES: \n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")
jogador = int(input("Qual sua jogada? "))
if jogador == computador



