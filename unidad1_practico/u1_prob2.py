'''
Descripccion:Realiza un programa en Python que indique si un número es divisible entre otro.
Nombre:Cinthia Valeria Gomez Luna
Fecha:6 de octubre del 2022
'''
# Mostraremos un mensaje de Bienvenida 
print("Hoy te enseñaremos los numeros que se pueden dividir entre otros")

#Se realizara las Funciones correspondientes 
num1=int(input("Numero 1:")) 
num2=int(input("Numero 2:"))
if num1%num2 == 0:
    print(num1,"es divicible entre",num2)
else:
    print(num1," no es divicible entre",num2)
    
    #Mensaje de despedida
    print("¡No es divicible intenta de Nuevo!")
  
