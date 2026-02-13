# Programa para calcular média de um aluno e mostrar a situação dele.
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print(f"Com as notas \033[36m{n1}\033[m e \033[36m{n2}\033[m, a média é \033[34m{media}  ")
if media < 5:
    print("\033[31mO aluno está reprovado")
elif media >= 7:
    print('\033[32mO aluno está aprovado\033[m')
elif 5 <= media < 7:
    print("O aluno está em recuperação")




