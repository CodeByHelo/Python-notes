# Jogo para comparar um valor digitado pelo teclado e outro sorteado para o computador, se forem igual
# o jogador ganha, se forem diferentes, o computador ganha.
import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
comp = random.randint(0,5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if num == comp:
    print('Parabéns, você ganhou!')
else:
    print('Ganhei! Eu pensei no número {} e você no número {}'.format(comp, num))