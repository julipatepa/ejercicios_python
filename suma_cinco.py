'''
4) Construya un algoritmo que, dado una entrada n, calcule la 

suma de los términos de una progresión aritmética como la 

que se muestra a continuación: 10; 15; 20; 25; 30 …..Tn. Esto 

es, su algoritmo debe calcular el valor: 10 + 15 + 20 + 25 + 30 

+ … + Tn. 

Pseudocódigo
'''
def suma_cinco(n):
	for i in range(10,n+5,5):
		print(i)
def main():
	n=int(input('ingrese n'))
	suma_cinco(n)
main()
