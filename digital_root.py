def digital_root(suma):
    while len(str(suma)) > 1:
        sumados = 0
        for a in str(suma):
            sumados += int(a)
        suma = sumados
    print (suma)


numero = input("le numero: ")
digital_root(int(numero))
