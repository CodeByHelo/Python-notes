# Pedra, papel, tesoura.
import random
from time import sleep
print('''Suas opções :
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
computador = random.randint(0,2)
print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")
sleep(1)
print("-=-" * 6)
if jogador == 0:
    print("Jogador jogou Pedra")
    print("Computador jogou ",end = "")
    if computador == 0:
        print("Pedra")
        print("EMPATE!!!")
    elif computador == 1:
        print("Papel")
        print("COMPUTADOR VENCE!")
    elif computador == 2:
        print("Tesoura")
        print("JOGADOR VENCE!")
    else:
        print("RESPOSTA INVÁLIDA!")
elif jogador == 1:
    print("Jogador jogou Papel")
    print("Computador jogou ", end = "")
    if computador == 0:
        print("Pedra")
        print("JOGADOR VENCE!")
    elif computador == 1:
        print("Papel")
        print("EMPATE!!!")
    elif computador == 2:
        print("Tesoura")
        print("COMPUTADOR VENCE!")
    else:
        print("RESPOSTA INVÁLIDA!")
elif jogador == 2:
    print("Jogador jogou tesoura")
    print("Computador jogou ", end = "")
    if computador == 0:
        print("Pedra")
        print("COMPUTADOR VENCE")
    elif computador == 1:
        print("Papel")
        print("JOGADOR VENCE")
    elif computador == 2:
        print("Tesoura")
        print("EMPATE!!!")
    else:
        print("RESPOSTA INVÁLIDA!")
print("-=-" * 6)





