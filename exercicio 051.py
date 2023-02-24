pTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = pTermo + (10 - 1) * razao

for c in range(pTermo,decimo + razao,razao):
    
    print(c)
print("FIM")