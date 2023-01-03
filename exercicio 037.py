numero = int(input("Digite um número:"))

print(" [ 1 ] Para binario")
print(" [ 2 ] Para hexadecimal")
print(" [ 3 ] Para octal")
escolha = input("Escolha uma opção para conversão")


if escolha == "1":    
    print("O número {} em binario é {}".format(numero,bin(numero)))
elif escolha == "2":    
    print("O número {} em hexadecimal é {}".format(numero,hex(numero)))
elif escolha == "3":    
    print("O número {} em octal é {}".format(numero,oct(numero)))
else:
    print("Opção invalida")  