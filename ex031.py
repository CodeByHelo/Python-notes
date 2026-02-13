# Programa para calcular o valor de uma passagem.
dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}'.format(dist))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('E o preço da sua passagem será de {}'.format(valor))