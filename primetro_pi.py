'''
Construya un DF tal que, dado como datos el radio y la altura de 

un cilindro, calcule e imprima el área y su volumen
'''
def area_volumen(a,r):
	pi=3.1416
	v=pi*r**2*a
	print('el volumen es:',v)
	a=2*pi*r*(a+r)
	print('el area es',a)
'''
def main():
	a=float(input('ingrese la altura'))
	r=float(input('ingrese el radio'))
	area_volumen(a,r)

main()
'''