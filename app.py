from operações import *

while True:
    print("-----------------------\n")
    print("Bem-vindo ao deixa que eu calculo\n")
    print("[0] Para Sair")
    print("[1] Para Somar")
    print("[2] Para Subtrair")
    print("[3] Para Dividir")
    print("[4] Para Multiplicar")

    opção = int(input("Digite a operação que você deseja:"))
    if opção ==1:
       n1 = int(input(" Digite o valor do primeiro número:"))
       n2 = int(input("Digite o valor do segundo número:"))
       resultado = somar(n1,n2)
       print (f" A sua soma é igual a:  {resultado}")

    elif opção == 2:
        n1 = int(input("Digite o valor do primeiro número:"))
        n2 = int(input("Digite o valor do segundo número:"))
        resultado = subtrair(n1,n2)
        print(f"A sua subtração é igual a:{resultado}")

    elif opção == 3:
        n1 = int(input("Digite o valor do primeiro número:"))
        n2 = int(input("Digite o valor do segundo número:"))
        resultado = dividir (n1,n2)
        print(f"A sua multiplicação é igual a:{resultado}")

    elif opção == 4:
        n1 = int(input("Digite o valor do primeiro número:"))
        n2 = int(input("Digite o valor do segundo número:"))
        resultado = multiplicação (n1,n2)
        print(f"A sua divisão é igual a:{resultado}")

    elif opção != [0,1,2,3,4]:
        print("Escolha inválida, digite outro número")


