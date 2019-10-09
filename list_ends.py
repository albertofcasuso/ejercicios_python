def nueva_lista(lista):
    fin = len(lista)
    fin_num = lista[fin-1]
    prin_num = lista[0]
    new_lista = []
    new_lista.append(prin_num)
    new_lista.append(fin_num)
    return print(new_lista)


a = [200, 10, 15, 20, 25, 56, 78, 26, 68, 9, 56, 273617326, 183182]
nueva_lista(a)
