import os
import time

#
#
#
# Abrir archivos open(lo que sea) especificando la ruta del archivo
# Leer archivos .read()
# Cerrar archivo despues de procesarlo .close()
"""
archivo = open('frutas.txt')
contenido = archivo.read()
archivo.close()
#print(contenido)
#print()
#print()

#
#
#
# Se puede hacer con with --- as
with open('frutas.txt', "r") as archivo:
    content = archivo.read()


#
#
# Para escribir \n es un salto de línea
with open('files/vegetales.txt', "w") as archivo:
    archivo.write("Tomate\nLechuga\nCebolla")
"""
with open('files/data.txt', 'a+') as file:
    file.seek(0)
    contenido = file.read()
    file.seek(0)
    file.write(contenido)
    file.write(contenido)


#
#
#
# Ver si existe un archivo
# os.path.exists() regresa True o false

while True:
    if os.path.exists('files/datan.txt'):
        print('Si existe')
    else:
        print('No existe')
    time.sleep(5)
