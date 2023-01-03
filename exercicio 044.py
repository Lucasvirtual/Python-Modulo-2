produto = float(input("Digite o preço do produto: R$"))
print("Escolha a opção de pagamento")
print("[ 1 ] Para pagamento à vista dinheiro/cheque 10% desconto")
print("[ 2 ] Para pagamento à vista cartão 5% desconto")
print("[ 3 ] Pagamento em até 2x no cartão preço normal ")
print("[ 4 ] Pagamento em até +3x no cartão 20% juros")

escolha = input("Digite um número para escolher: ")

if escolha == "1":
    avista = produto * 0.10
    novoAvista = produto - avista
    print("Você pagará R${} ".format(novoAvista))
elif escolha == "2":
    avistacartao = produto * 0.05
    novoAvistac = produto - avistacartao
    print("Você pagará R${}".format(novoAvistac))
elif escolha == "3":
    print("Parcelando em 2x você pagará R${}".format(produto))
elif escolha == "4":
    parcelado = produto * 0.20
    novoParcelado = produto + parcelado
    print("Você pagará R${}".format(novoParcelado))
else:
    print("Digite um número válido")
    