from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print("[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR")
    opção = int(input(">>>>> Qual é a sua opção? "))
    if opção == 1:
        print(f"A soma entre {n1} e {n2} é igual a {n1 + n2}")
        sleep(2)
    elif opção == 2:
        print(f"A multiplicação entre {n1} e {n2} é igual a {n1 * n2}")
        sleep(2)
    elif opção == 3:
        if n1 == n2:
            print("Os valores são iguais.")
        else:
            if n1 > n2:
                 maior = n1
            elif n2 > n1:
                 maior = n2
            print(f"Entre {n1} e {n2}, o maior valor é {maior}")
        sleep(1)
    elif opção == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        sleep(1)
    elif opção == 5:
        print("Finalizando...")
        sleep(1)
        print("Fim do programa, volte sempre!")
    else:
        print("Opção inválida. Tente novamente.")
    print("=-=" * 10)
