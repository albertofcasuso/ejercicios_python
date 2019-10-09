# Con def se define la funcion y en con return es el resultado que da.
# puede tener valores por defecto entre los paréntesis del inicio

def prim_num(numero):
    rango = range(2,numero)
    divisores = []

    for index in rango:
        if numero % index == 0:
            divisores.append(index)

    if len(divisores) == 0:
        return print("Es primo")
    else:
        return print("Los divisores son: "+ str(divisores))

a = int(input("Dame un numero: "))
prim_num(a)
