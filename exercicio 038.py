numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))

if numero1 > numero2:
    print("O maior número é: {}".format(numero1))
elif numero2 > numero1:
    print("O maior número é: {}".format(numero2))
else:
    print("Os dois valores são iguais")