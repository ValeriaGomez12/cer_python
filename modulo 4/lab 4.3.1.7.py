'''
Descripccion: Proyectar y escribir funciones parametrizadas.
Autor: Valeria Gomez
Fecha:4 de octubre del 2022
'''



def isYearLeap(años):
	if años % 4 != 0:
		return False
	elif años % 100 != 0:
		return True
	elif años % 400 != 0:
		return False
	else:
		return True

def daysInMonth(años,meses):
	if años < 1582 or meses < 1 or meses > 12:
		return None
	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = dias[meses - 1]
	if meses == 2 and isYearLeap(años):
		res = 29
	return res

testaños = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresultados = [28, 29, 31, 30]
for i in range(len(testaños)):
	yr = testaños[i]
	mo = testmonths[i]
	print(yr,mo,"-> ",end="")
	resultado = daysInMonth(yr, mo)
	if resultado == testresultados[i]:
		print("Es correcto")
	else:
		print("Fallido")