pergunta = " "
contIdade = 0
contSexo = 0
contF = 0
while pergunta != "N":
    
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        contIdade += 1
    sexo = str(input("Qual o sexo ? [M/F] "))
    if sexo == "M":
        contSexo += 1
    if sexo == "F" and idade <= 20:
        contF += 1


    pergunta = str(input("Quer continuar ? [S/N] "))

print("Total de pessoas com mais de 18 anos: {}".format(contIdade))
print("Ao todo temos {} homens cadastrados".format(contSexo))
print("E temos {} mulheres com menos de 20 anos".format(contF))