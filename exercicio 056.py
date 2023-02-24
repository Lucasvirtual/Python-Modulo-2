idade = 0
somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for c in range(1,5):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: [F ou M]: "))
    somaidade += idade

    if c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade > 20:
        totmulher20 += 1



    



media = somaidade / 4




print("a media do grupo é: {}".format(media))
print("O homem mais velho é: {}".format(nomevelho))
print("A quantidade de mulheres menores que tem 20 anos são: {}".format(totmulher20))