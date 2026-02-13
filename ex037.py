# Programa para converter um número para binário, octal ou hexadecimal.
num = int(input("Digite um número inteiro: "))
print("Escolha um das bases para conversão:")
print("[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL")
opção = int(input("Sua opção: "))
if opção == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opção == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválida. Tente novamente!")


