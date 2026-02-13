# Programa para ler a velocidade de um carro, se for maior que 80km/h mostra uma mensagem
# dizendo que foi multado, a multa vai custar R$7,00 por cada km acima do limite.
vel = int(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
