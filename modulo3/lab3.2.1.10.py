'''
Descripccion: Utilizar la instrucción continue en los bucles.
Autor: Valeria Gomez
Fecha: 29 de sep del 2022
'''


    
from re import L


userWord = input("Ingresa la pañabra")
userWord = userWord.upper()

for letter in userWord:
    if letter== "A":
        continue
    elif letter=="E":
        continue
    elif letter=="I":
        continue
    elif letter=="0":
        continue
    else:
        print(letter)
    

