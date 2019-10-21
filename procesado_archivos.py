#
#
#
# Abrir archivos open(lo que sea) especificando la ruta del archivo
# Leer archivos .read()
# Cerrar archivo despues de procesarlo .close()

archivo = open('frutas.txt')
contenido = archivo.read()
archivo.close()
print(contenido)
print()
print()

#
#
#
# Se puede hacer con with

with open('frutas.txt') as archivo:
    content = archivo.read()

print(content)