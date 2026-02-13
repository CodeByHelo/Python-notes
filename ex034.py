# Programa para dar um aumento para um funcionário, dependendo do seu salário atual.
sal = float(input('Qual é o salário do funcionário? '))
if sal <= 1250:
    nsal: float = sal * 1.15
else:
    nsal: float = sal * 1.10
print('Quem ganhava R${} passa a ganhar R${:.2f} agora.'.format(sal, nsal))