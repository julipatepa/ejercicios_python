'''
Se desea leer por teclado un número comprendido entre 0 y 10 

(inclusive) y se desea visualizar si el número es par o impar.
)
'''
def par_impar(v,opcion):
	funcion={
	       1 : 100*v,
       	2 : 100**v,
	       3 : 100/v
	
	}
	resultado = funcion.get(opcion,0)
	print(resultado)
'''
def main():
	v=int(input('ingrese un valor'))
	opcion=int(input('ingrese tipo de calculo'))
	par_impar(v,opcion)

main()
'''
