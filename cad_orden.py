'''
Ejercicio 6.9. Definir una función que, dadas dos cadenas de caracteres como parámetros,

devuelva como resultado la cadena que sea anterior en orden alfabético. [Ej: para los

argumentos ‘kde’ y ‘gnome’ debería devolver al programa principal ‘gnome
'''
def cadena_anterior(cad,cad1):
	resultado:""
	resultado1:""
	for i in range(len(cad),len(cad1)):
		if cad<cad1:
			print(cad)
			

		else:
			print(cad1)
		
		
'''
def main():
	cad="kde"
	cad1="gnome"
	resultado=cadena_anterior(cad,cad1)
main()
'''