'''
Escribir un algoritmo que invierta los dígitos de un número 

positivo entero. Usar operadores módulo y división para ir 

obteniendo los dígitos uno a uno. Por ejemplo, si se ingresa 

37368 debe retornar el numero 86373
'''
n='86373'
for i in range(len(n)-1,-1,-1):
	print(int(n[i]))
		
