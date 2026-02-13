#Programa para converter uma temperatura digitada em °C para °F.

tempc = float(input('Informe a temperatura em °C: '))
tempf:float = (tempc * (1.8)) + 32

print('A temperatura de {:.2f} °C, corresponde a {:.2f} °F.'.format(tempc, tempf))