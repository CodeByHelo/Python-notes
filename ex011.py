#Programa que leia as medidas de uma parede, sua área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta pinta uma área de 2m^2.

l = float(input('Qual a comprimento da parede? '))
h = float(input('Qual a altura da parede? '))

area = l * h
tinta = area / 2

print('Essa parede mede {} metros quadrados.'.format(area))
print('Para uma parede que mede {}x{}, será necessário {:.2f}L de tinta para pintá-la.'.format(l, h, tinta))