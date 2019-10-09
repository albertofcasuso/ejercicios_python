import random

a = random.randint(1, 1000)
salir = 0
intentos = 0

while salir != "exit":
    salir = input("Adivina el número o escribe \"exit\" para salir: ")
    try:
        int_salir = int(salir)
        if int_salir == a:
            if intentos == 0:
                print("¡¡¡Has acertado a la primera!!!")
                a = random.randint(1, 1000)
            else:
                intentos += 1
                a = random.randint(1, 1000)
                print("Has acertado en "+str(intentos)+" intentos.")
                intentos = 0

        elif int_salir < a:
            print("Más arriba")
            intentos += 1

        elif int_salir > a:
            print("Más abajo")
            intentos += 1

    except ValueError:
        if salir == "exit":
            if intentos == 1:
                print("Lo has intentado "+str(intentos)+" vez.")
                salir == "exit"
            elif intentos == 0:
                print("Ni siquiera lo has intentado :( ")
                salir == "exit"
            else:
                print("Lo has intentado "+str(intentos)+" veces.")
                salir = "exit"
        else:
            print("no entiendo")
