numero = int(input("Digite um número: "))
mult = 0
for c in range (1,numero + 1):
    if numero % c == 0:
        print("Multiplo de", c)
        mult += 1
if mult == 2:
    print("é primo")
else:
    print("Não é primo")