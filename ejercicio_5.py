# Comparar dos tablas Darle dos tablas y que saque que elementos estan repetidos

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lista = []

for num in a:
    if num in b:
        lista.append(num)

print (lista)
