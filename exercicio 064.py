numero = 0
acumulador = 0
soma = 0

numero = int(input("Digite um número: "))

while numero != 999:    
    soma += numero
    acumulador += 1
    numero = int(input("Digite um número: "))

print("A soma dos números é: ",soma)
print("A quantidade de números que foram digitados: ",acumulador)  