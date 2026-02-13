# Programa para ler um valor em metros e converter para centímetros  e milímetros.

m = int(input('Digite o valor em m: '))
cm = m * 100
mm = m * 1000

print('{} metros = {} centímetros'.format(m, cm))
print('{} metros = {} milímetros'.format(m, mm))