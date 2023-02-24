numero = int(input("Digite um número: "))
termo1 = 0
termo2 = 1
print("{} {}".format(termo1, termo2))
c = 3
while c <= numero:
    termo3 = termo1 + termo2
    print("{}".format(termo3))
    termo1 = termo2
    termo2 = termo3
    c += 1
print("FIM")