'''
Descripccion: Utilizar el bucle while.
Autor: Valeria Gomez
Fecha: 29 de sep del 2022
'''

bloques = int(input("Ingrese el número de bloques: "))
altura = 0

while bloques > 0:
    longitudNecesariaDelNivel = altura + 1

    if longitudNecesariaDelNivel <= bloques:
        bloques -= longitudNecesariaDelNivel
        altura += 1
    else:
        break

print("La altura de la pirámide:", altura)
print("Sobran:", bloques, "bloque(s).")