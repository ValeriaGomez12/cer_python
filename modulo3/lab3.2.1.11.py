'''
Descripccion: Utilizar la instrucción continue en los bucles.
Autor: Valeria Gomez
Fecha: 29 de sep del 2022
'''
palabraSinVocal = ""
userWord = ""

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter== "I":
        continue
    elif letter== "O":
        continue
    elif letter== "U":
        continue
    else:
        palabraSinVocal += letter

print(palabraSinVocal)