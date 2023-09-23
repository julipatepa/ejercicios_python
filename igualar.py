'''
Ejercicio 7.4. Definir una función ‘suma_vectores’ que, dadas por parámetro dos tuplas que 

representan vectores de igual dimensión, devuelva como resultado la tupla que representa 

su suma. [La suma de vectores ( u1, u2, u3 ) y ( v1, v2, v3 ), se puede calcular como el 

vector que resulta de sumar sus componentes homólogas: ( u1 + v1 , u2 + v2 , u3 + v3 ) ].

'''
def suma_vectores(tup,tup1):
	for i in tup:
		print (i)
		
		for x in tup1:
			res=i+j
			print (res)
'''
def main():
    tup=[u1,u2,u3]
    tup1=[v1,v2,v3]
    suma_vectores(tup,tup1)
main()
'''