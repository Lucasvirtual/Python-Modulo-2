valor = int(input("Digite o valor que deseja sacar: R$ "))
n50 = n20 = n10 = n1 = 0
while True:
    if valor >= 50:
        valor -= 50
        n50 += 1
    else:
        if valor >= 20:
            valor -= 20
            n20 += 1
        else:
            if valor >= 10:
                valor -= 10
                n10 += 1
            else:
                if valor >= 1:
                    valor -= 1
                    n1 += 1
    if valor == 0:
        break
print("Você receberá {} notas de 50, {} de 20, {} de 10 e {} de 1.".format(n50,n20,n10,n1))