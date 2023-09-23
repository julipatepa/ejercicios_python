'''
. Realice un diagrama de flujo que convierta millas a 

kilómetros. Se sabe que una milla equivale a 1.609344 

kilómetros
'''
def milla_a_km(m):
	km=1
	km*=1.60934
	m=km*m
	print('las millas ingresadas en km es: ',m)
'''
def main():
	m=float(input('ingrese la cantidad en millas'))
	milla_a_km(m)
main()
'''