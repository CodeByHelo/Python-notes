#Programa que leia cateto oposto e adjacente e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Comprimento do cateto Oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}.'.format(hypot(co, ca)))
