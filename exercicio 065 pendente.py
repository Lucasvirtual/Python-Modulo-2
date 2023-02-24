soma = 0
c = 0
maior = menor = numero = 0

while c < 5:    
    numero = int(input("Digite um número: "))
    
    soma += numero
    c += 1
    media = soma / c
    
    if c == 1:
        maior = menor = numero
    else:
        if numero > numero:
            maior = numero
        if numero < numero:
            menor = numero

print("A media dos números é: ",media)
print("O maior número foi: ",maior)
print("O menor número foi: ",menor)