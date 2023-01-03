from datetime import date
ano = int(input("Ano de nascimento"))
atual = date.today().year
idade = atual - ano
print("O atleta tem {} anos ".format(idade))

if idade <= 9:
    print("Classificação mirim")
elif idade <= 14:
    print("Classificação infantil")
elif idade <= 19:
    print("Classificação junior")
elif idade <= 25:
    print("Classificação senior")
elif idade > 25:
    print("Classificação master")