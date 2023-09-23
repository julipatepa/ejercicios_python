'''
Desarrolle un algoritmo para determinar si un año leído por 

teclado es o no bisiesto
Todos los años bisiestos son divisibles entre 4. Aquellos años que son divisibles entre 4, pero no entre 100, son bisiestos. Los años que son divisibles entre 100, pero no entre 400, no son bisiestos. Sin embargo, los años divisibles entre 100 y entre 400 sí que son bisiestos
'''
def bisiesto(año):
	if año%4==0 and año%100!=0:
	  print('es bisiesto',año)
	elif  año%100==0 and año%400==0:
	 print('es bisiesto',año)
	else:
		print('no es bisiesto')
'''
def main():
	 año=int(input('ibgrese el año'))
	 bisiesto(año)

main()
	''' 
	 
   
		
	