def fibonacci(cantidad):
    lista = range(1, cantidad)
    fibos = [1]
    a = 0
    b = 1
    for num in lista:
        c = a + b
        fibos.append(c)
        a = b
        b = c
    return print (fibos)


cuantos = int(input("¿Cuántos fibos quieres? "))
fibonacci(cuantos)
