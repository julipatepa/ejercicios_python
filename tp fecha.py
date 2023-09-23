def es_bisiesto(anio): #verifica si es bisiesto
    return anio%400==0 or anio%100 !=0 and anio%4==0
      

def validacion_fecha (days,month,year): #verifica si la fecha existe y si es superior a 2023
    bisi = es_bisiesto(year)
    if (month == 2 and bisi and days <= 29  and days > 0 and year >= 2023):
        
        return True
    
    elif (month == 2 and days <= 28 and days>0 and year >= 2023):
        
        return True
    
    elif (month == 4 and days <= 30 and days > 0 and year >= 2023
          or month == 6 and days <= 30 and days > 0 and year >= 2023
          or month == 9 and days <= 30 and days > 0 and year >= 2023
          or month == 11 and days <= 30 and days > 0 and year >= 2023):
        
        return True
    
    elif (month == 1 and days <= 31 and days > 0 and year >= 2023
          or month == 3 and days <= 31 and days > 0 and year >= 2023
          or month == 5 and days <= 31 and days > 0 and year >= 2023
          or month == 7 and days <= 31 and days > 0 and year >= 2023
          or month== 8 and days <= 31 and days > 0 and year >= 2023
          or month == 10 and days <= 31 and days > 0 and year >= 2023
          or month == 12 and days <= 31 and days > 0 and year >= 2023):
        
        return True
    
    else :
        return False


def validation_date (): #pide los datos y devuelve lo que se busca xd
    day = input('ingrese el dia, mes y año (dd mm aaaa): ')
    date = day.split(' ')
    int_date = [int(x) for x in date]
    
    verification = validacion_fecha(int_date[0],int_date[1],int_date[2])

    if verification == True:
        print ('es verdadero xd, aca se agregaria a un diccionario y pasaria a la siguiente')
    else:
        print ('fecha incorrecta, por favor separe dia, mes y año por espacios, y que sea superior al año 2023')
        validation_date()


validation_date()

