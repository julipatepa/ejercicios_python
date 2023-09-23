'''
Un proveedor de estéreos ofrece un descuento del 10% sobre 

el precio sin IGV, de algún aparato si esta cuesta $2000 o más. 

Además, independientemente de esto, ofrece un 5% de 

descuento adicional sobre el precio si la marca es “NOSY
Determinar cuánto pagará, con IGV incluido, un cliente 

cualquiera por la compra de su aparato. IGV = 20% 
'''
def descuento(precio,marca):
	if precio>=2000 and marca=='nosy':
		precio*=0.90
		precio*=0.95
		precio*=1.20
		print('el precio a pagar es:',precio) 
	elif precio>=2000 and marca!='nosy':
		precio*=0.95
		precio*=1.20
		print(precio)
	elif precio<2000 and marca=='nosy':
		precio*=0.95
		precio*=1.20
		print(precio)
	elif precio<2000 and marca!='nosy':
		precio*=1.20
		print(precio)
'''
def main():
	precio=float(input('ingrese el valor'))
	marca=input('ingrese la marca')
	descuento(precio,marca)
	
main()
'''
	
	
	
