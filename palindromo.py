# Te dice si una palabra e sun palindromo
string = input("Dame una palabra: ")
palindromo=string[::-1]
if string == palindromo:
    print("Es un palindromo")
else:
    print("No es un palíndromo")
