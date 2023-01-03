nome = str(input("Qual seu nome ?"))
if nome == "Lucas":
    print("Que nome bonito !")

elif nome == "Amauricio" or nome == "Andre" or nome == "Maria":
    print("Nomes populares no brasil")
else:
    print("Nome feio")

print("Tenha um bom dia {}".format(nome))
