nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2)/2
print("Tirando {} e {} a média do aluno é {}".format(nota1,nota2,media))
if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")