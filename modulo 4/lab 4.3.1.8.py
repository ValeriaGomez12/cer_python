'''
Descripccion: Proyectar y escribir funciones con parámetros.
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

def daysInMonth(años, meses):
	if años < 1582 or meses < 1 or meses > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[meses - 1]
	if meses == 2 and isYearLeap(años):
		res = 29
	return res

def dayOfYear(años, meses, dias):
	days = 0
	for m in range(1, meses):
		md = daysInMonth(años, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(años, meses)
	if dias >= 1 and dias <= md:
		return days + dias
	else:
		return None

print(dayOfYear(2000, 12, 31))