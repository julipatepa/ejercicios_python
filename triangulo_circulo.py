'''
Algoritmo que permita efectuar el cálculo del área de un 

círculo o un triángulo equilátero según la opción seleccionada 

por el usuario a través de un menú, además se deben ingresar 

los datos adicionales que se requieran para el cálculo del área. 
'''
def circulo_triangulo(circulo,triangulo):
	 if circulo=='si':
	 	r=float(input('ingrese el radio'))
	 	pi=3.1416
	 	area=pi*r**2
	 	print('el area del circulo es',area)
	 if triangulo=='si':
	 	a=float(input('ingrese un lado del triangulo'))
	 	areat= ( (3 ** 0.5)/ 4) * a**2
	 	print(areat)
	 else:
	 	print('ah ingresado dos veces que no no se haran calculos')
def main():
	triangulo=str(input('ingrese si o no para calcular el area del triangulo'))
	circulo=str(input('ingrese si o no para calcular el area de un circulo'))
	
	circulo_triangulo(circulo,triangulo)
	
main()