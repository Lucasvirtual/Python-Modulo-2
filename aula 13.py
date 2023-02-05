nome = input("Digite seu nome: ")
contar = int(input("Quantas vezes você quer contar ?"))
c = 0
s = 0
for c in range(1,contar + 1 ):
    print("{} {}".format(c,nome))
    numero = int(input("Digite um numero para somar: "))
    s = s + numero
print("Finalizado")

print(s)