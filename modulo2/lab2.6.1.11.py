'''
Descripccion:Mejorar la habilidad de
implementar números, operadores y operaciones aritméticas en Python
Autor: Valeria Gomez
Fecha: 22 de sep

'''


hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

 

# calcula los minutos y los convierte a una cadena

minutos=str((min+dura) %60)

# calcula los minutos totales y luego lo convierte a horas y despues a una cadena

horas= str( ((hora*60 + min + dura)//60) % 24)

 

 

print("Hora: " +horas +":" +minutos)