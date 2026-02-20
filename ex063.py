print("-" * 25)
print("Sequência de Fibonacci")
print("-" * 25)
num = int(input("Quantos termos você quer mostrar? "))
n1 = 0
n2 = 1
c = 1
print(n1,"->",n2, end = " -> ")
while c <= num - 2:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end = " -> ")
    c+=1
print("FIM!")
