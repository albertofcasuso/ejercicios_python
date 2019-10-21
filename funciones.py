#
#
#
# Funciones con varios parámetros

def area(a, b):
    return a+b
print (area('culo','pedo'))

#
#
#
#
# Argumentos keyword defines con igual al llamar la funcion
# puedes asignar un valor por defecto a la funcion

def area(a, b=100):
    return a+b
print(area(a=50))


#
#
#
# Si defines la funcion con *args, puedes meter todos los argumentos que quieras
# espues los llamas con 'args'
def media(*args):
    return sum(args)/len(args)

media(10,20,30,40,50,60,70,80,90,100,150,120,130,140)


def ordenada(*args):
    args = [elem.upper() for elem in args]
    return sorted(args)

print(ordenada("nieve","algo","besos"))