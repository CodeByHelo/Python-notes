print("-" * 30)
print("LOJA DA HELO".center(30))
print("-" * 30)

total = produto1000 = contador = 0

while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: "))
    total += preço
    contador += 1
    if contador == 1:
        barato = produto
        valor = preço
    else:
        if preço < valor:
            barato = produto
            valor = preço

    if preço >= 1000:
        produto1000 += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print(" FIM DO PROGRAMA ".center(30, "-"))
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {produto1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa {valor:.2f}")
