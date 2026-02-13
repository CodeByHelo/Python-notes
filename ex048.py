#Soma dos números ímpares multiplos de 3 entre 1 e 500
somatotal = 0
somanumeros = 0
for c in range (0,501,3):
    if c % 2 == 1:
        somatotal += c
        somanumeros += 1
print(f"A soma de todos os {somanumeros} números é igual a {somatotal}")