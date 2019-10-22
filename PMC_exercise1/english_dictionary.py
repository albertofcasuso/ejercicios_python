import json
# Libreria para comparar strings
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    #######
    # Lo haces lowercase para que no de un error al meter mayúsculas o minúsculas
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("La palabra no está en el diccionario. Quizás quisiste decir %s (s/n) " %
                   get_close_matches(word, data.keys())[0])
        if yn == "s":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "La palabra no está en el diccionario."
        else:
            return "WTF Dude. I didn't understand."
    else:
        return "La palabra no está en el diccionario."


while True:
    print("####################")
    consulta = input("Dame una palabra (/end para salir): ")
    if consulta == "/end":
        break
    else:
        output = translate(consulta)
        if type(output) == list:
            a = 1
            for num in output:
                print("\n"+str(a)+"_"+str(num)+"\n")
                a += 1
        else:
            print(output)
