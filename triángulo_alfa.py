'''
Si se conoce la longitud de dos de los lados de un triángulo (b 

y c) y el ángulo entre ellos (alfa), expresado en grados 

sexagesimales, la longitud del tercer lado (a) se calcula por la 

fórmula:

a

2 = b

2 + c

2 – 2bc*cos(alfa)
'''
import math 
def lado_triangulo_alfa(b,c,alfa):
	pi=3.1416
	a=(b**2+c**2-2*b*c*math.cos(alfa*pi/180))**0.50
	print(a)
'''
def main():
	b=float(input('ingrese el valor del lado b'))
	c=float(input('ingrese el valor del lado c'))
	alfa=float(input('ingrese el valor de alfa'))
	lado_triangulo_alfa(b,c,alfa)
main()
'''
