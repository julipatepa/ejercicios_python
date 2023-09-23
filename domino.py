"""
Ejercicio 7.3. Definir una función ‘encaja_domino’, que reciba por parámetro dos tuplas que 

representan fichas de dominó y devuelva un resultado booleano que indique si encajan o no. 

[Ej: las fichas (3, 4) y (4, 1) encajan, porque coinciden en el número 4. Ídem (4, 4) y (5, 4) ]
"""
def encaja_domino(tup,tup1):
  for i,x in tup,tup1:
    print(i)
    print(x)
    if i [-1]==x[-1]:
        print(i+i)
        
'''             
def main():
    tup=('3,4','4,1')
    tup1=("4,4","5,4")
    encaja_domino(tup,tup1)
main()
'''