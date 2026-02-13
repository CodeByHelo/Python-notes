#Programa para calcular valor da prestação de uma casa e negar o empréstimo se a prestação for maior que 30% do
# salário do comprador.
valor_casa = float(input("Qual o valor da casa? R$"))
salário = float(input("Salário do comprador: "))
anos = int(input("Quantos anos de financiamento: "))
prestação = valor_casa / (12 * anos)
print(f"Para pagar uma casa de \033[36m{round(valor_casa, 2)}\033[m em \033[36m{anos}\033[m anos", end = " ")
print(f"a prestação será de \033[36m{round(prestação, 2)}\033[m")
if prestação > 0.3 * salário:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo APROVADO!")