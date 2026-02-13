# Programa para saber se determinados segmentos podem formar um triângulo.
print('\033[31m-=-\033[m' * 10)
print("Analisador de triângulos")
print("\033[31m-=-\033[m" * 10)
n1 = float(input("\033[36mPrimeiro segmento:\033[m "))
n2 = float(input("\033[36mSegundo segmento:\033[m "))
n3 = float(input("\033[36mTerceiro segmento: \033[m"))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print("Os segmentos acima podem formar um triângulo!")
else:
    print("Os segmentos acima não podem formar um triângulo.")

