# Programa para classificar atletas pela idade.
from datetime import date
ano = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = ano - nasc
print(f"O atleta tem {idade} anos.")
print("Categoria: ", end = "")
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <=19:
    print("JUNIOR")
elif idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")
