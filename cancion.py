# Imprime todas las lineas de 99 elefantes
elefantes = input("¿Cuantos elefantes se balanceaban? ")
elefantes = int(elefantes)
while elefantes > 0:
    if elefantes == 1:
        print(str(elefantes)+" elefante se balanceaba.")
        print()
        elefantes -= 1
    else:
        print(str(elefantes)+" elefantes se balanceaban.")
        print()
        elefantes -= 1
