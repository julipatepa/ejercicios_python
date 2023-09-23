'''
Algoritmo, que dada una fecha del año 2000 (representada por 

el día, el mes y el año en formato numérico dd/mm/aaaa), 

calcule el día siguiente. Asuma que el mes tiene 30 días
abril, junio, septiembre y noviembre. Los meses con 31 días son: enero, marzo, mayo, julio, agosto, octubre y diciembre
'''
import es_bisiesto
def mes_dia(dia,año,mes):
	if es_bisiesto==True and mes==2 and dia==29:
	   	dia=1
	   	mes+=1
	   	print('dia/mes',dia,mes)
	elif mes ==4 or mes ==6 or mes==7 or mes==11 and dia ==30:
	   	mes+=1
	   	dia=1
	   	print('dia/mes',dia,mes)
	elif mes !=4 or mes !=6 or mes!=7 or mes!=11 and dia ==31:
	    dia=1
	    mes+=1
	    print('dia/mes',dia,mes)
 '''   
def main():
	dia=int(input('ingrese el dia'))
	año=int(input('ingrese el año'))
	mes=int(input('ingrese el mes'))
	mes_dia(dia,año,mes)
main()
'''
     
	


		
		
		
		
		
		
		
	
