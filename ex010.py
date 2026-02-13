# Programa que lê quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar.
# U$$1,0 = R$3,27

rs = float(input('Quantos reais você tem? R$'))
dol = rs/3.27

print('Com R${:.2f}, você consegue comprar U$${:.2f}'.format(rs, dol))