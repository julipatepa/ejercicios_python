'''
Calcular el monto a pagar por un artículo si se tiene como 

datos de entrada la cantidad de docenas que compra y el costo 

por unidad de este artículo
'''
def costo_unidad(cu,cd):
	cd*=cu*12
	print('el precio a pagar es:',cd)
'''
def main():
	cu=float(input('ingrese costo por unidad'))
	cd=float(input('ingrese la cabtidad d2 docenas'))
	costo_unidad(cu,cd)
main()
'''
	