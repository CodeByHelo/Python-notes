# Programa para ler se um número é par ou impar
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))