'''
Descripccion:Proyectar y escribir funciones con parámetros.
Autor: Valeria Gomez
Fecha:4 de octubre del 2022
'''

import os


def isYearLeap (años) :
  if años % 4 != 0:
    return False
  elif años % 100 != 0:
    return True
  elif años % 400 != 0:
    return False 
  else:
    return True 

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
  yr = testData[i]
  print(yr,"->",end="")
  result = isYearLeap(yr)
  if result == testResults[i]:
    print("Es Correcto")
  else:
    print("Fallido")