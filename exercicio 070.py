pergunta = " "
total = 0
maior = 0
contPreco = 0
menor = 0
barato = " "

while pergunta != "N":
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: "))
    pergunta = str(input("Quer Continuar ? [S/N]"))
    
    total += preco
    if preco > 1000:
        contPreco += 1
    
    if preco < menor:
        menor = preco
        barato = produto

print("O total da compra foi R${}".format(total))
print("Temos {} produtos custando mais de R$1000.00".format(contPreco))
print("O produto mais barato foi {} que custa R${}".format(barato,menor))