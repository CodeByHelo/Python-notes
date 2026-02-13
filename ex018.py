# Programa para ler um ângulo e mostrar o seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, math.tan(math.radians(ang))))