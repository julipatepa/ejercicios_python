'''
Construya un diagrama de flujo (DF) que resuelva un problema 

que tiene una gasolinera. Los dispensadores de esta registran lo 

que “surten” en galones, pero el precio de la gasolina está fijado

en litros. El DF debe calcular e imprimir lo que hay que cobrarle 

al cliente
'''
def galones(ga):
	lts=ga*3.78
	precio=lts*4.50
	print('usted cargo',ga,'litros'  ,'el total a pagar es',precio)
'''
def main():
	ga=int(input('ingrese la cntidad de galones'))
	galones(ga)
main()
'''