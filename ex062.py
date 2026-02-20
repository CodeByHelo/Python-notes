print("Gerador de PA")
print("-=-" * 10)

primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("Razão da PA: "))
print(primeiro,end = " -> ")
for c in range(1,10):
    primeiro += razão
    print(primeiro, end = " -> " )
print("PAUSA")
quant = 1
total = 10
while quant != 0:
    c = 1
    quant = int(input("Quantos termos você quer mostrar a mais? "))
    total += quant
    while c <= quant:
        primeiro += razão
        print(primeiro, end = " -> ")
        c +=1
    print("PAUSA!")
print(f"Progressão com {total} termos")





