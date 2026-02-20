print("Gerador de PA")
print("-=-" * 10)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
c = 1
print(primeiro, end =" -> ")
while c < 10:
    primeiro += razão
    c += 1
    print(primeiro, end = " -> ")
print("FIM!")

