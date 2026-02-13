#Programa que calcula o aluguel de um carro por dias e km rodados.

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))

total: float = (60 * dias) + (0.15 *km)

print('O total a pagar é de R${:.2f}'.format(total))