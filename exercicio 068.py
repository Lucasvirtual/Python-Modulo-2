import random
c = 0
cont = 0

while True:
    numero = int(input("Digite um valor: "))
    
    computador = random.randint(0,11)
    soma = numero + computador
    escolha = " "

    while escolha not in "PI":
        escolha = str(input("Par ou Ímpar ? [P/I] "))
    print("Você jogou {} e o computador {}, Total de {} ".format(numero,computador,soma))    
    print("PAR" if soma % 2 == 0 else "IMPAR")
        
    if escolha == "P":
        if soma % 2 == 0:
        
            cont += 1
                
            print("Você ganhou")
        
        else:       
            print("Você perdeu")

    elif escolha == "I":
        if soma % 2 == 1:
                
            print("Você venceu")
            cont += 1
        else:
            print("Você perdeu")
            break