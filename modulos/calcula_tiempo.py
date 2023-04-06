from datetime import datetime, timedelta
import math


class Datatime13lunas:
    def __init__(self):        
        #Fecha de inicio inicia el 26 de Julio del año 1991 se supone q yo estaba en el 
        #estomago de mi madre 
        date_string = '1991-7-26 00:00:0'
        fecha_init = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        #fecha Actual 
        #date_string2 = '2023-4-4 00:00:0'
        #fecha_init2 = datetime.strptime(date_string2, '%Y-%m-%d %H:%M:%S')
        #fecha_hoy = fecha_init2
        fecha_hoy = datetime.now()

        #Calcula el numero de dias trascurridos al momento de la fecha actual
        self.tiempo_trascurrido = fecha_hoy.date() - fecha_init.date()

        
    #Genera el año calen13
    def numero_de_an(self):        
        an_tras = int(self.tiempo_trascurrido.days/365)
        return an_tras
    
    #Genera el mes calen13
    def numero_de_meses(self):        
        mes = ((((self.tiempo_trascurrido.days%365)) - int((6 * self.numero_de_an())/24)) / 28)
        multiplier = 10 ** 0
        mesaml =  math.ceil(mes * multiplier) / multiplier
        
        #print(((self.tiempo_trascurrido.days%364)-int((6 * self.numero_de_an())/24))-int((6 * self.numero_de_an())/24) / 28)
        return int(mesaml)
    





    #Genera el dia calen13
    def numero_de_dias(self):        
        mes_mod = ((self.tiempo_trascurrido.days%365)-int((6 * self.numero_de_an())/24)) % 28
        if mes_mod == 0:
            return 28
        return mes_mod

    #Genera del año de nacimiento a la fecha actual 
    def numero_de_dias_total(self):                
        return self.tiempo_trascurrido.days








