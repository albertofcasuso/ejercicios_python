#!/usr/bin/python3

import random

comando = "0000"
numero_maquina = random.randint(1000, 9999)
intentos = 0


def verifica(numm, numu):
    cowbull = [0, 0]
    posX = 0
    if int(numm) == int(numu):
        cowbull[0] = 4
        cowbull[1] = 0
    else:
        for x in str(numu):
            if x in str(numm):
                if str(numu)[posX] == str(numm)[posX]:
                    cowbull[0] += 1
                else:
                    cowbull[1] += 1
            posX += 1

    return cowbull


while comando != "exit":
    print()
    comando = input("Adivina el numero: ")
    if comando == "exit":
        print("Adios")
        break
    else:
        vacas = verifica(numero_maquina, comando)
        if vacas[0] == 4:
            intentos += 1
            print()
            print("Has ganado despues de "+str(intentos)+" intentos")
            break
        else:
            intentos += 1
            print()
            print(str(vacas[0])+" vacas, "+str(vacas[1])+" toros.")
