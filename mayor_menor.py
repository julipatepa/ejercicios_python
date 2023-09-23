'''
Crear un algoritmo, que dado N números enteros ingresados 

por teclado determine cuál de ellos es el menor y mayor 

respectivamente
'''
#def menor_mayor(num,num2):
a='si'
while a=='si':
		num=int(input('ingrese el primer numero'))
		num2=int(input('ingrese el primer numero'))
		if num>num2:
			print('el mayor es ',num)
		else:
			print('el mayor es',num2)
		a=input('ingrese no para terminar o si para continuar')
'''
def main():
	num=int(input('ingrese el primer numero'))
	num2=int(input('ingrese el primer numero'))
	menor_mayor(num,num2)
main()
'''
		
	
	