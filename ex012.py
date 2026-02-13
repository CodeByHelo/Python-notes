#Calcular 5% de desconto em um produto digitado pelo usuário.
from shlex import join

price = float(input('Qual é o preço do produto? '))
nprice: float = price * 0.95
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(price, nprice))