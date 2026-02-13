# Programa para ver se um triângulo é equilátero, isósceles ou escaleno.
n1 = int(input("Primeiro segmento: "))
n2 = int(input("Segundo segmento: "))
n3 = int(input("Terceiro segmento: "))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end = "")
    if n1 == n2 == n3:
        print("EQUILÁTERO!")
    elif n1 == n2 or n3 == n2 or n1 == n3:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos acima NÃO podem formar um triângulo.")