frase = str(input("Digite uma frase: "))
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Palindromo")
else:
    print("não é um Palindromo")
