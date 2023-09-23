'''
 Escriba un algoritmo tal que dado como datos X números 

enteros, obtenga el número de ceros que hay entre estos 

números. Por ejemplo, si se ingresa 6 datos: 9 0 4 8 0 1

El algoritmo arroja que hay 2 ceros
'''
def cont_cero(n):
	c=0
	for i in range(1,n+1):
		num=int(input('ingrese  numero'))
		if num==0:
			c = c+1
		print('la cantidad de ceros es:',c)		
def main():
	n=int(input('ingrese cant de numeros'))
	cont_cero(n)
main()