'''
Escribir un algoritmo que imprima los 10 primeros números 

primos comenzando en 2 e imprima también sus respectivos 

cubos. Por ejemplo: 2 – 8 ; 3 – 27; 5 –125
'''
import primo
def cuadrado(c,d):
	for i in range(c,d):
	    if primo.es_primo(i)==True:
	        i=i**2
		    print(i)
def main():
	c=2
	d=10
	cuadrado(c,d)
main()
	
		
