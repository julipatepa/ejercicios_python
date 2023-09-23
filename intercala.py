def intercala_chr(cadena, caracter):
       resultado = ""
       for i in range(len(cadena)):
             resultado += cadena[i]
             if i != len(cadena) - 1:
                       resultado += caracter
       return resultado
'''
def main():
		cadena_original = "veamos"
        caracter_insertar = "-"
        resultado = intercala_chr(cadena_original,          caracter_insertar)
        print(resultado)
main()
'''