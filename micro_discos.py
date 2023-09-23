'''
Elaborar un algoritmo que permita calcular el número de micro 

discos 3 .5 necesarios para hacer una copia de seguridad, de la 

información almacenada en un disco cuya capacidad se conoce. 

Hay que considerar que el disco duro está lleno de información, 

además expresado en gigabyte. Un micro disco tiene 1.44 

megabyte y un gigabyte es igual a 1,024 megabyte.(Vinuesa, 

1966)

Procederemos a determinar los datos de entrada, la salida y 

variables intermedias, obsérvese.

Entrada Identificador

Número de Gigabyte del Disco Duro GB

Número de Megabyte del Disco Duro MG

Salida

Número de Micro Disco 3.5 MD

El proceso de cálculo para determinar el número de Megabytes 

(MG) dado la cantidad de Gigabytes (GB) es MG = 1024 x GB,

esto se puede determinar también si se aplica la regla de tres 

simple. Para calcular el número de Micro discos de 3.5 se 

procede a dividir el número de Megabytes (MD) calculados entre 

1.44 que es la capacidad de un solo Micro disco, así:

MD = MG / 1.44
'''
import math
def discos(gb,mb,md):
	
	mb=gb*1024
	md=mb/1.44
	print(math.ceil(md))

'''
def main():
	gb=float(input('ingrese capacidad del disco en gb'))
	mb=0
	md=0
	discos(gb,mb,md)
main()
'''
	
	
	
	

