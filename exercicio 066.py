cont = 0
numero = 0
soma = 0

while True:
    numero = int(input("Digite números: "))
    
    if numero == 999:
        break
    cont += 1
    soma += numero
print("Foram digitados {} números, e a soma entre eles foi {}".format(cont,soma))