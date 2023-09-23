'''
Ejercicio 6.8. Definir una función ‘separa_miles’ que, dada por parámetro una cadena de 

caracteres que contiene un largo número entero, devuelva como resultado la cadena con las 

separaciones de miles incluidas en el número. [Ej: para el argumento ‘1234567890’ debería 

devolver al programa principal ‘1.234.567.890’ 
'''
def separa_miles(cad,car):
	resultado=""
	for i in range(len(cad)):
	      resultado+=cad[i]
	      if i==len(cad)-4 or i==len(cad)-7 or i==len(cad)-10:
		      resultado+=car
		
		
	return resultado	
'''
def main():
	cad="1234567890"
	car="."
	resultado=separa_miles(cad,car)
	print(resultado)
	
	

main()
'''
	    
		