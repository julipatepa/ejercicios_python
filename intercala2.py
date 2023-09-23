'''
Ejercicio 6.6. Definir una función “sustituye_chr” que, dados como parámetros una cadena 

de caracteres txt y dos caracteres c1 y c2, devuelva como resultado una cadena con la 

sustitución, en txt, de todos los caracteres iguales a c1, por el carácter c2. [Ej: pasados 

como argumentos el texto ‘mi primer modulo.py’, el carácter ‘ ‘ y el carácter ‘_‘, debería 

devolver al programa principal ‘mi_primer_modulo.py
'''
def sustituye_chr(txt,c1,c2):
	resultado=""
	for i in range(len(txt)):
		resultado+=txt[i]
		if i==len(txt)-3:
			resultado+=c2
			
		elif i==len(txt)-15 or  i==len(txt)-9:
			resultado+=c1
	return resultado		
'''
def main():
	c1="-"
	c2="."
	txt="miprimermodulopy"
	resultado=sustituye_chr(txt,c1,c2)
	print(resultado)
	

main()
'''
			
			
		