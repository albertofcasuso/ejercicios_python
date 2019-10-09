import random


def password(longitud):
    simbolos = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    contra = []
    for num in range(0, longitud):
        caracter = random.choice(simbolos)
        contra.append(caracter)
        contraseña = "".join(contra[::1])

    return print(contraseña)


contra = input("De que longitud quieres el password: ")
password(int(contra))
