'''
Dado el sueldo de un trabajador, aplique un aumento del 15% si 

su sueldo es inferior a $1000. Imprima el sueldo que percibirá.

'''
def aumento(s):
	a=1000
	if s<a:
		resultado=s*0.15+1000
		print(resultado)
'''
def main():
	s=float(input('ingrese su sueldo'))
	aumento(s)
main()
'''
		
		