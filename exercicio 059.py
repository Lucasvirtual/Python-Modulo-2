numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
opcao = 0
maior = 0

print("Digite [1] para somar")
print("Digite [2] para multiplicar")
print("Digite [3] para maior")
print("Digite [4] para novos números")
print("Digite [5] para sair do programa")
print("------------------------------------------")

while opcao != 5:

    opcao = int(input("Digite a opção que deseja: "))
    if opcao == 1:
        soma = numero1 + numero2
        print("A soma de {} + {} é: {}".format(numero1,numero2,soma))

    if opcao == 2:
        multi = numero1 * numero2
        print("A multiplicação de {} * {} é : {}".format(numero1,numero2,multi))
    
    if opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2    
        
        print("O maior números dos dois é: ",maior)
    
    if opcao == 4:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
    
    