'''
 Leer tres números enteros y, si el primero de ellos es negativo, 

calcular el producto de los tres, en caso contrario calcular la 

suma de ellos.
'''
def sum_pro(a,b,c):
	if a<0:
		resultado=a*b*c
		print(resultado)
	else:
		resultado=a+b+c
		print(resultado)
'''
def main():
	a=float(input('ingrese num'))
	b=float(input('ingrese 2do num'))
	c=float(input('ingrese el 3er num'))
	sum_pro(a,b,c)
	
main()
'''