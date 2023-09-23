'''
Construya un algoritmo que, dados tres números, muestre el 

mensaje “IGUALES” si la suma de los dos primeros es igual 

al otro número y el mensaje “DISTINTOS” en caso contrario
'''
def sumas_iguales(a,b,c):
	if a+b==c:
		print('la suma de los dos primeros numeros es igual al tercero')
	else:
		print('son distintos')
'''
def main():
	a=int(input('ingrese el primer valor'))
	b=int(input('ingrese el segundo valor'))
	c=int(input('ingrese el tercero valor'))
	sumas_iguales(a,b,c)
main()
'''