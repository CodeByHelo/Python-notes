#Calcular o reajuste de 15% no salário de um funcionário.

sal = float(input('Qual é o salário do funcionário? '))
nsal:float = sal * 1.15

print('Um funcionário que ganhava R${}, com aumento de 15%, passa a receber R${:.2f}.'.format(sal, nsal))