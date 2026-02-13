
print("========= Helo's Store ========")
valor = float(input("Valor das compras: "))
print("FORMAS DE PAGAMENTO\n"
      "[ 1 ] à vista dinheiro ou cheque\n"
      "[ 2 ] à vista cartão\n"
      "[ 3 ] 2x no cartão\n"
      "[ 4 ] 3x ou mais no cartão")
opção = int(input("Qual é a opção? "))
if opção == 1:
    valor = valor * 0.90
    print(f"O valor a ser pago será de R${valor:.2f}, com 10% de desconto. ")
elif opção == 2:
    valor = valor * 0.95
    print(f"O valor a ser pago será de R${valor:.2f}, com 5% de desconto.")
elif opção == 3:
    parcela = valor / 2
    print(f"Sua compra de R${valor} será parcelada em 2 vezes de R${parcela}")
elif opção == 4:
    valor = valor * 1.20
    totalparc = int(input("Em quantas parcelas você quer dividir? "))
    parc = valor / totalparc
    print(f"O valor a ser pago será de R${valor:.2f} em {totalparc} parcelas de R${parc}, com 20% de juros.")
else:
    print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")