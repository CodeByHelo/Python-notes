# Ler 7 anos de nascimento de pessoas e no final mostrar quantos são maiores e quantos são menores.
import datetime
anoatual = datetime.date.today().year
maior = 0; menor = 0
for c in range(1,8):
    ano = int(input(f"Em que ano a {c} pessoa nasceu? "))
    idade = anoatual - ano
    if idade > 21:
        maior += 1
    else:
        menor += 1
print(f"Ao todo, tivemos {maior} pessoas maiores de idade e\n {menor} menores de idade")