print("=" * 30)
print("BANCO DA HELO".center(30))
print("=" * 30)

din = int(input("Qual valor você quer sacar? "))

notas50 = notas20 = notas10 = notas1 = 0

while True:
    if din >= 50:
        notas50 = din//50
        din = din % 50
        print(f"Total de {notas50} cédulas de 50")
        if din % 50 == 0:
            break
    if din >= 20:
        notas20 = din//20
        din %= 20
        print(f"Total de {notas20} cédulas de 20")
        if din % 20 == 0:
            break
    if din >= 10:
        notas10 = din//10
        din = din % 10
        print(f"Total de {notas10} cédulas de 10")
        if din % 10 == 0:
            break
    else:
        print(f"Total de {din} cédulas de 1")
        break







