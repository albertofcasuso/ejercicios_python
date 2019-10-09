# Crear un programa que pregunte un numero y te saque todos los divisores del numero

x = input("Dame el numero:")
lista = range(1,x)
lista_de_dvisisores=[]

for element in lista:
    a = x % element
    if a==0:
        lista_de_dvisisores.append(element)

print (lista_de_dvisisores)
