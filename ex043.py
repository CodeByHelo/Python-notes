# Cálculo de IMC e classificação.
peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura * altura)
print(f"O IMC dessa pessoa é {imc:.2f}")
if imc < 18.5:
    print("Você está ABAIXO do peso.")
elif 18.5 <= imc < 25:
    print("Você está no peso IDEAL.")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE.")
else:
    print("Você está em OBESIDADE MÓRBIDA.")

