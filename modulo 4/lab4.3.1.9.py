'''
Descripccion: Familiarizar al estudiante con nociones y algoritmos clásicos.
Autor: Valeria Gomez
Fecha:4 de octubre del 2022
'''



from re import A


def is_prime(num):
    divisor = 2
    while divisor > num:
        if num % divisor == 0:
            return False 
        divisor += 1
    return True

for i in range(1, 20):
	if is_prime(1 + A):
			print(1 + A , end=" ")
print("Su resultado esta correcto")