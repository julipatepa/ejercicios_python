'''
Se tiene los puntos A y B en el cuadrante positivo 

del plano cartesiano, elabore el algoritmo que permita obtener 

la distancia entre A y B.

'''
def hipotenusa(cx,cy,cx1,cy1):
	dc1=cx-cx1
	dc=cy-cy1
	h=( ( dc**2)+(dc1**2))**0.5
	print(h)
'''
def main():
	cx=float(input('ingrese la distancia A'))
	cx1=float(input('ingrese la segunda distancia A'))
	cy=float(input('ingrese la distancia B'))
	cy1=float(input('ingrese la segunda distancia B'))
	hipotenusa(cx,cx1,cy,cy1)
	
main()
'''