import random

pc = random.randint(0, 10)

acertou = False
palpites = 0

while not acertou:
    numero = int(input("Acerte o número"))
    print("o número que você escolheu",numero)
    
    palpites += 1

    if numero == pc:
       acertou = True
       print("-------------------------------------")
       print("Você acertou")
       print("o número que o pc sorteou",pc) 
    else:
        print("você errou tente novamente")

print("Acertou com {} tentativas, Parabéns".format(palpites))