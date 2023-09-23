'''
Algoritmo, que dado dos números “a” y “b”, muestre sus 

valores en orden de menor a mayor
'''
def orden_num(a,b):
	if a>b:
		print(b)
		print(a)
	elif a<b:
		print(a)
		print(b)
	else:
		print('los numeros son iguales')
'''
def main():
	a=float(input('ingrese el primer valor:'))
	b=float(input('ingrese el segundo valor:'))
	orden_num(a,b)
main()
'''
