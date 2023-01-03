from datetime import date
nascimento = int(input("Digite o ano de seu nascimento:"))
atual = date.today().year
idade = atual - nascimento
print("Quem nasceu em {} terá {} anos em {}".format(nascimento,idade,atual))
if idade >= 18:
    print("Precisa se alistar")
elif idade <= 18:
    print("Ainda não precisa se alistar, falta {} anos ".format(18 - idade))
else:
    print("")