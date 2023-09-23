'''
Elaborar un algoritmo que permita ingresar el número de 

partidos ganados, perdidos y empatados, por ABC club en el 

torneo apertura, se debe de mostrar su puntaje total, 

teniendo en cuenta que por cada partido ganado obtendrá 3 

puntos, empatado 1 punto y perdido 0 puntos
'''
def partidos(pg,pp,pe):
	pg*=3
	pe*=1
	pp*=0
	resultado=pg+pp+pe
	print(resultado)
'''
def main():
	pg=int(input("ingrese los partidos ganados"))
	pp=int(input("ingrese los partidos perdidos"))
	pe=int(input("ingrese los partidos empatados"))
	partidos(pg,pp,pe)
   
main()
'''