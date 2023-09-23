'''
Cuáles y cuántos son los números primos comprendidos 

entre 1 y 1000? Construya su diagrama de flujo.
'''
def es_primo(a,b):
	for i in range(a,b+1):
		if i%1==0 and i%1==0 and i%3!=0 and i%2!=0 :
			
			print(i)
		elif i==2 or i==3:
		   print (i)
		else:
			print('nos es primo')

def main():
	a=2
	b=int(input('ingrese con el nro quw finalizara el rango'))
	es_primo(a,b)
main()

