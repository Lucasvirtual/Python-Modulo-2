casa = float(input("Qual valor da casa que você quer comprar ?"))
salario = float(input("Qual seu salário ?"))
anos = int(input("Com quantos anos você pretende pagar ?"))
minimo = salario * 30 / 100
prestacao = casa / (anos * 12)
if prestacao <= minimo:
    print("Emprestimo concedido")
else:
    print("Emprestimo negado")

