# Programa para calcular a data de alistamento para o sexo masculino.
from datetime import date
anoatual = date.today().year
nasc = int(input("Ano de nascimento:"))
idade = anoatual - nasc
alistamento = nasc + 18
sexo = str(input("Digite seu sexo [M/F]:"))
print(f"Quem nasceu em {nasc} tem {idade} anos em {anoatual}")
if sexo == "F":
        print('O alistamento para o sexo feminino não é obrigatório.')
elif sexo == "M":
    if idade < 18:
        print(f"Ainda faltam {18 - idade} anos para o alistamento.")
        print(f"Seu alistamento será em {alistamento}")
    elif idade > 18:
        print(f"Você já deveria ter se alistado há {idade - 18} anos")
        print(f"Seu alistamento foi em {alistamento}")
    else:
        print(f"Você deve se alistar IMEDIATAMENTE!")