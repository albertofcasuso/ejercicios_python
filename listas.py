temps = [221,234,450,569,345,123,145]

""" En una sola linea puedes hacer el for, incluso añadir un if o 
algun otro condicional """

new_temps = [x/10 for x in temps if x > 250]
print(new_temps)

#
#
# Devuelve solo los elementos de un tipo dentro de una lista
array = [99,'algo',95,94,'no data']

def only_numers(lista):
    # Para ver si es un numero o string (if isinstance(x,str))
    numbers = [x for x in lista if not isinstance(x,int)]
    return numbers

print(only_numers(array))

#
#
#
# Devuelve solo los numeros que no sean negativos

def positivos(lista):
    positivo = [x for x in lista if x >=0]
    return positivo

#
#
#
# Si dentro de la compresion va un if else, el for va al final
# si hay varias condicionales solo hay un for, no varios


def ceros(lista):
   return [0 if isinstance(x,str) else x for x in lista ]

print(ceros(array))

#
#
#
# La suma dentro de los numeros de una lista

array = ['1.2','2.5','3.4','5.6','6.7']
def suma(lista):
    return sum([float(x)for x in lista])
print(suma(array))