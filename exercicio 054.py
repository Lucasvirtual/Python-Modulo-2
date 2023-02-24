maior = 0
menor = 0
for c in range(0,7):
    ano = int(input("Digite o ano de nascimento: "))
    if ano <= 2005:
        maior = maior + 1       
    else:
        menor = menor + 1




print("{} são maiores de idade".format(maior))
print("{} não são maiores de idade".format(menor))