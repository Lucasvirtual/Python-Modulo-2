soma = 0
c = 0
maior = menor = numero = 0

while c < 5:    
    numero = int(input("Digite um número: "))
    
    soma += numero
    c += 1
    
    
    if c == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / c
print("A media dos números é: ",media)
print("O maior número foi: ",maior)
print("O menor número foi: ",menor)