'''
Se desea leer por teclado un número comprendido entre 0 y 10 

(inclusive) y se desea visualizar si el número es par o impar.

'''
def par_impar2(n):
	dicc={
	1:'impar',
	2:'par',
	3:'impar',
	4:'par',
	5:'impar',
	6:'par',
	7:'impar',
	8:'par',
	9:'impar',
	10:'par'
	}
	print(dicc.get(n,'numero fuera de rango'))
'''
def main():
	n=int(input('ingrese el valor numerico'))
	par_impar2(n)

main()
'''