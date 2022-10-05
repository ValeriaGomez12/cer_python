'''
Descripccion: Mejorar las habilidades del estudiante para definir, utilizar y probar funciones.
Autor: Valeria Gomez
Fecha:4 de octubre del 2022
'''


def litros_100km_to_miles_galones(litros):
    miles = 100 * 1000 / 1609.344
    galones = litros/ 3.785411784 
    return miles / galones


def miles_gallon_to_liters_100km(miles):
    litros = 3.785411784 
    kim = miles * 1609.344 / 1000 
    km100 = kim / 100
    return litros / km100

print(litros_100km_to_miles_galones(3.9))
print(litros_100km_to_miles_galones(7.5))
print(litros_100km_to_miles_galones(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))