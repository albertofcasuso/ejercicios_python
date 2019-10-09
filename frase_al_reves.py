def al_reves(frase):
    palabras = frase.split()
    reves_al = " ".join(palabras[::-1])
    return print(str(reves_al))


frase = input("Escribe la foking frase: ")
al_reves(frase)
