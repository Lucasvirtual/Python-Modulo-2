cont = 0
numero = 0
c = 0
while cont < 10:   
    numero = int(input("Digite um número para multiplicar: "))
    
    if numero == -1:
        break   
    for c in range(1,11):
        print("{} X {} = {}".format(numero,c,numero * c))