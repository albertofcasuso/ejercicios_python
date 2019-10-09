# True si es primo
def primo(num):
    num = int(num)
    a = 0
    for num_ in range(2, num):
        if num % num_ == 0:
            a += 1
        if a >> 0:
            return False
        else:
            return True


# True si NO 1 ni 7
def uno_siete(num):
    num = str(num)
    if (not "1" in num and not "7" in num):
        return True
    else:
        return False


# Suma todos y True si no es mayor a 10
def suma(num):
    suma = 0

    for num in str(num):
        suma += int(num)

    if suma > 10:
        return False
    else:
        return True


# Suma de los dos primeros digitos es impar?
def dosprimeros(num):
    if len(str(num)) >= 2:
        suma = 0
        dos = str(num)[:2]
        for a in dos:
            suma += int(a)
        if suma % 2 != 0:
            return True
        else:
            return False


def penultimo(num):
    penultimo = len(str(num)) - 1
    if int(str(num)[:penultimo]) % 2 == 0:
        return True
    else:
        return False


def ultimo_numero(num):
    longitud = len(str(num))
    ultimo = int(str(num)[longitud-1])
    if longitud == ultimo:
        return True
    else:
        return False


for x in range(0, 1000):
    if primo(x):
        if uno_siete(x):
            if suma(x):
                if dosprimeros(x):
                    if penultimo(x):
                        if ultimo_numero(x):
                            print(x)
