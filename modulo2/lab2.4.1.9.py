'''
Descripccion:familiarizarse con el concepto de variables y trabajar con ellas. 
Autor: Valeria Gomez 
Fecha:22 de sep

'''


kilometers = 12.25
miles = 7.38
'''
    1 milla = 1.61 kilometros
    7.32 millas = ?
    
    1 milla = 1.61 kilometros
    ?       = 12.25 kil
    
    
'''

miles_to_kilometers = miles * 1.61 / 1
kilometers_to_miles = 12.25 * 1 /1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")