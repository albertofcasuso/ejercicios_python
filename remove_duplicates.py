import random


def sin_dups(cuantos):
    cuantos = int(cuantos)
    lista = []
    sindups = []
    for num in range(1, cuantos):
        lista.append(random.randint(1, 10000))

    for num in lista:
        if not num in sindups:
            sindups.append(num)

    longitud = len(sindups)
    return print(str(sindups) + " Hay " + str(longitud)+" numeros en la lista.")


estos = input("Cuantos numeros habra en la lista: ")
sin_dups(estos)
