# Programa para ler maior e menor valor entre 3 números lidos pelo teclado.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
maior = a
if b < menor:
    menor = b
if b > maior:
    maior = b
if c < menor:
    menor = c
if c > maior:
    maior = c
print('O maior valor digitado foi: {}.'.format(maior))
print('O menor valor digitado foi: {}.'.format(menor))