#Criar um programa que leia um número real e mostre a sua porção inteira.
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))
