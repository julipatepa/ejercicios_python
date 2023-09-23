'''
Escriba un algoritmo que lea un número entero N y calcule el 

resultado de la siguiente serie
1-1/2+1/3+1/4...+1/n
'''
def fraccion(n):
	res=0
	for i in range(1,n+1):
		if i%2==0:
			res=res-(1/i)
			
		else:
			res=res+(1/i)
	print(res)
def main():
	n=int(input('ingresa n'))
	fraccion(n)
main()
		