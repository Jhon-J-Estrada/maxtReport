import tkinter as tk
from tkinter import ttk,messagebox,END,Toplevel
from model.report import crear_table, borrar_table
from model.report import Report, guardar_report, listar_report,editar_report,eliminar
from model.mes_repor import Report_mes, guardar_report_mes, editar_report_mes, eliminar_mes,listar_report_mes
from model.mes_repor import crear_table_mes, borrar_table_mes
from .calcula_tiempo import Datatime13lunas


#def barra_menu(root):
    
    
    
#class Frames 
class Frame(tk.Frame):
    def __init__(self,root = None):
        #Menu
        barra_menu = tk.Menu(root)
        root.config(menu=barra_menu, width=300, height= 300)

        menu_inicio = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label = 'Dias', menu=menu_inicio)

        menu_inicio.add_command(label='Crear Tabla Registro',command=crear_table)
        menu_inicio.add_command(label='Eliminar Tabla Registro', command=borrar_table)
        menu_inicio.add_command(label='Salir', command=root.destroy)
   
        menu_mes = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label = 'Mes', menu=menu_mes)

        menu_mes.add_command(label = 'Reporte Mes', command=self.report_mes)
        menu_mes.add_command(label = 'Crear Tabla Mes', command=crear_table_mes)
        menu_mes.add_command(label = 'Borrar Tabla Mes', command=borrar_table_mes)

        #menu_inicio.add_cascade(label = 'config')
        #menu_inicio.add_cascade(label = 'Ayuda')



        super().__init__(root, width=900, height=700)
        self.root = root
        #Fechas
        self.fechas13 = Datatime13lunas()

        #Numero de dias 
        self.numdias = self.fechas13.numero_de_dias_total()
        self.dianame = f'{self.fechas13.numero_de_an()}-{self.fechas13.numero_de_meses()}-{self.fechas13.numero_de_dias()}'
        
        self.root.title(f" {self.numdias}  {self.dianame}")
        self.pack()
        self.config(bg='#333')

        self.valuedia = ''

        
        
        
        
        #FORMA FRAME INIT 
        self.lis_report()
         
        self.campos_labels()
        self.campos_input()
        self.campos_buttos()

        #self.lis_report()
        self.campos_buttos_list()
        
        #variable id del report
        self.id_report_lis = None
        self.id_report_lis_mes = None
        #ACTION
        


        
        
#---------------------------- FORAT FRAME MES -------------------------        

#ejecuta nueva ventana 
    def report_mes(self):
        self.ventana_mes = Toplevel()
        self.ventana_mes.geometry("1500x700")
        self.ventana_mes.title("Repor Fin de Mes ")
        self.campos_input_mes(self.ventana_mes)
        self.campos_labels_mes(self.ventana_mes)
        self.campos_buttos_mes(self.ventana_mes)
        self.lis_report_mes()
        self.campos_buttos_list_mes()


#Forma los impus del reporte por mes 
    def campos_input_mes(self,ventana_mes):

        self.entry_odjet = tk.Text(ventana_mes,
                   height = 8,
                   width = 50,
                   )
        
        
        #self.entry_report = tk.Entry(self, textvariable= self.valuedia)
        self.entry_odjet.config( font=('Arial',12))
        self.entry_odjet.grid(row=0,column=1, padx=10, pady=10, columnspan=2)

            
        self.entry_nummes = tk.Text(ventana_mes,
                   height = 1,
                   width = 5,
                   )
        self.entry_nummes.config( font=('Arial',12))
        self.entry_nummes.grid(row=1,column=4, padx=10, pady=10, columnspan=2)

        #self.code = tk.StringVar()
        self.entry_apren_mes = tk.Text(ventana_mes,
                   height = 8,
                   width = 50,
                   )
        #self.entry_report_code = tk.Entry(self, textvariable=self.code)
        self.entry_apren_mes.config(width=50, font=('Arial',12))
        self.entry_apren_mes.grid(row=1,column=1, padx=10, pady=10, columnspan=2)

        
#Titulos de los campos Inpus Ventana Mes 
    def campos_labels_mes(self,ventana_mes):
        #labels
        self.label_report = tk.Label(ventana_mes, text='Objetivos: ')
        self.label_report.config(font=('Arial',12,'bold'))
        self.label_report.grid(row=0, column=0, padx=10, pady=10)

        self.label_report = tk.Label(ventana_mes, text='List años: ')
        self.label_report.config(font=('Arial',12,'bold'))
        self.label_report.grid(row=4, column=0, padx=10, pady=10)

        text_data = f'Año  {self.fechas13.numero_de_an()}  Mes {self.fechas13.numero_de_meses()}  Dia  {self.numdias}'
        self.label_report = tk.Label(ventana_mes, text=text_data)
        self.label_report.config(font=('Arial',23,'bold'),background='#357' , fg='#eee')
        self.label_report.grid(row=0, column=4, padx=10, pady=10)

        self.label_report = tk.Label(ventana_mes, text='Num:3-5-7 ')
        self.label_report.config(font=('Arial',12,'bold'),anchor='sw')
        self.label_report.grid(row=1, column=5, padx=10, pady=10)

        self.label_report_code = tk.Label(ventana_mes, text='Apren: ')
        self.label_report_code.config(font=('Arial',12,'bold'))
        self.label_report_code.grid(row=1, column=0, padx=10, pady=10)


#Forma los botonoes de action en un nuevo repor 
    def campos_buttos_mes(self,ventana_mes):        
        
        self.buttom_guardar_mes = tk.Button(ventana_mes, text='Guardar', command=self.guardar_datos_mes)
        self.buttom_guardar_mes.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#DAD5D6',
                                bg='#1658A2',
                                cursor='hand2',
                                activebackground='#3586DF'
                                )
        self.buttom_guardar_mes.grid(row=3, column=1, padx=10, pady=10)


        self.buttom_cancel_mes = tk.Button(ventana_mes, text='Cancelar', command=self.desabilitar_campos)
        self.buttom_cancel_mes.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#BD152E',
                                bg='#158645',
                                cursor='hand2',
                                activebackground='#E15370'
                                )
        self.buttom_cancel_mes.grid(row=3, column=2, padx=10, pady=10 )


    
#Guardar Datos repor mes 
    def guardar_datos_mes(self):
               
        #crando el objeto repor
        repor = Report_mes(
            self.numdias,
            self.dianame,               
            self.entry_nummes.get("1.0",END),
            self.entry_odjet.get("1.0",END),            
            self.entry_apren_mes.get("1.0",END),               
            
        )       
        

        if self.id_report_lis_mes == None:
           guardar_report_mes(repor)
        else:
            editar_report_mes(repor, self.id_report_lis_mes)
            
        

        
        
        self.desabilitar_campos_mes()
        self.lis_report_mes()
        

#ceando lista de dias 
    def lis_report_mes(self):

        #Lista los report 
        self.listar_report_mes = listar_report_mes()

        #Invertir        

        self.lis_mes = ttk.Treeview(self.ventana_mes,
                                       columns = ('Numdia','Namedia','Valuedia','Repor','Apren'))
        self.lis_mes.grid(row=4, column=1, columnspan=5, sticky='nes')

        #scrollbar para la table de repor si exeden los 10 registros 
        self.scroll = ttk.Scrollbar(self.ventana_mes, orient='vertical', command= self.lis_mes.yview)
        self.scroll.grid(row=4, column=5, sticky='nse')
        self.lis_mes.config(yscrollcommand=self.scroll.set)
        
        

        self.lis_mes.heading('#1', text='NUMDIA')
        self.lis_mes.heading('#2', text='NAMEMES')
        self.lis_mes.heading('#3', text='VALUEDIA')
        self.lis_mes.heading('#4', text='OBJE')        
        self.lis_mes.heading('#5', text='APREN')

        self.lis_mes.column("#0" ,width = 0)
        
        

        

        #Iterar lista report
        for r in self.listar_report_mes:            
            
                #Inser a la table            
            self.lis_mes.insert('',0,text=r[0], values=(
                r[1], r[2], r[3], r[4], r[5]
            ))    


#Froma los botones de editar eliminar por cada item de la lista de los meses 
    def campos_buttos_list_mes(self):        
        self.buttom_editar_mes = tk.Button(self.ventana_mes, text='Ver', command= self.editar_report_viw_mes)
        self.buttom_editar_mes.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#DAD5D6',
                                bg='#158645',
                                cursor='hand2',
                                activebackground='#35BD6F'
                                )
        self.buttom_editar_mes.grid(row=5, column=1, padx=10, pady=10)
        
        self.buttom_eliminar_mes = tk.Button(self.ventana_mes, text='Eliminar', command=self.eliminar_repor_viw_mes)
        self.buttom_eliminar_mes.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#BD152E',
                                bg='#158645',
                                cursor='hand2',
                                activebackground='#E15370'
                                )
        self.buttom_eliminar_mes.grid(row=5, column=2, padx=10, pady=10 )


#Editar item de la lista de report 
    def editar_report_viw_mes(self):      
        self.desabilitar_campos_mes()  
        try:
            self.id_report_lis_mes = self.lis_mes.item(self.lis_mes.selection())['text']
            self.value_mes = self.lis_mes.item(self.lis_mes.selection())['values'][2]
            self.objet_mes = self.lis_mes.item(self.lis_mes.selection())['values'][3]
            self.apren_mes = self.lis_mes.item(self.lis_mes.selection())['values'][4]
            

            
            self.entry_nummes.insert(tk.END,self.value_mes)
            self.entry_odjet.insert(tk.END, self.objet_mes)
            self.entry_apren_mes.insert(tk.END, self.apren_mes)
            
            

        except:
            title = 'Editar Reporte'
            mesaje = 'Seeccione un repor a editar'
            messagebox.showinfo(title=title, message=mesaje)
        

        
        
 #Desabilita los campos de acuerdo a la action del User 
    def desabilitar_campos_mes(self):
        self.id_report_lis_mes = None
        #Limpiar Campos de texto
        self.entry_odjet.delete("1.0",END)
        self.entry_nummes.delete("1.0",END)
        self.entry_apren_mes.delete("1.0",END)

#Elimiar item de la lista de report
    def eliminar_repor_viw_mes(self):
        try:
            self.id_report_mes = self.lis_mes.item(self.lis_mes.selection())['text']
            eliminar_mes(self.id_report_mes)

            self.lis_report_mes()

            self.id_report_lis = None
            
        except:
            title = 'Eliminar Reporte'
            mesaje = 'Seeccione un repor a Eliminar'
            messagebox.showinfo(title=title, message=mesaje)


#---------------------------- FORAT FRAME DIA -------------------------


  

#Forma los campos inpus en el frame 
    def campos_input(self):

        self.entry_report = tk.Text(self,
                   height = 5,
                   width = 50,
                   )
        
        
        #self.entry_report = tk.Entry(self, textvariable= self.valuedia)
        self.entry_report.config( font=('Arial',12))
        self.entry_report.grid(row=0,column=1, padx=10, pady=10, columnspan=2)

            
        self.entry_num = tk.Text(self,
                   height = 1,
                   width = 5,
                   )
        self.entry_num.config( font=('Arial',12))
        self.entry_num.grid(row=0,column=2, padx=10, pady=10, columnspan=2)

        #self.code = tk.StringVar()
        self.entry_code = tk.Text(self,
                   height = 5,
                   width = 50,
                   )
        #self.entry_report_code = tk.Entry(self, textvariable=self.code)
        self.entry_code.config(width=50, font=('Arial',12))
        self.entry_code.grid(row=1,column=1, padx=10, pady=10, columnspan=2)

        #self.apren = tk.StringVar()
        self.entry_apren = tk.Text(self,
                   height = 5,
                   width = 50,
                   )
        #self.entry_report_apren = tk.Entry(self, textvariable= self.apren)
        self.entry_apren.config(width=50, font=('Arial',12))
        self.entry_apren.grid(row=2,column=1, padx=10, pady=10, columnspan=2)

#Forma los botonoes de action en un nuevo repor 
    def campos_buttos(self):        
        
        self.buttom_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.buttom_guardar.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#DAD5D6',
                                bg='#1658A2',
                                cursor='hand2',
                                activebackground='#3586DF'
                                )
        self.buttom_guardar.grid(row=3, column=1, padx=10, pady=10)


        self.buttom_cancel = tk.Button(self, text='Cancelar', command=self.desabilitar_campos)
        self.buttom_cancel.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#BD152E',
                                bg='#158645',
                                cursor='hand2',
                                activebackground='#E15370'
                                )
        self.buttom_cancel.grid(row=3, column=2, padx=10, pady=10 )

#Froma los botones de editar eliminar por cada item de la lista de dias repor 
    def campos_buttos_list(self):        
        self.buttom_editar = tk.Button(self, text='Ver', command= self.editar_report_viw)
        self.buttom_editar.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#DAD5D6',
                                bg='#158645',
                                cursor='hand2',
                                activebackground='#35BD6F'
                                )
        self.buttom_editar.grid(row=5, column=0, padx=10, pady=10)
        
        self.buttom_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_repor_viw)
        self.buttom_eliminar.config(width=20,
                                font=('Arial', 12,'bold'),
                                fg='#BD152E',
                                bg='#158645',
                                cursor='hand2',
                                activebackground='#E15370'
                                )
        self.buttom_eliminar.grid(row=5, column=2, padx=10, pady=10 )
 
#Titulos de los campos Inpus
    def campos_labels(self):
        #labels
        self.label_report = tk.Label(self, text='Report: ')
        self.label_report.config(font=('Arial',12,'bold'))
        self.label_report.grid(row=0, column=0, padx=10, pady=10)

        self.label_report = tk.Label(self, text='Num:3-5-7 ')
        self.label_report.config(font=('Arial',12,'bold'))
        self.label_report.grid(row=0, column=3, padx=10, pady=10)

        self.label_report_code = tk.Label(self, text='Code: ')
        self.label_report_code.config(font=('Arial',12,'bold'))
        self.label_report_code.grid(row=1, column=0, padx=10, pady=10)

        self.label_report_apren = tk.Label(self, text='Apren: ')
        self.label_report_apren.config(font=('Arial',12,'bold'))
        self.label_report_apren.grid(row=2, column=0, padx=10, pady=10)        

#ceando lista de dias 
    def lis_report(self):

        #Lista los report 
        self.listar_report = listar_report()

        #Invertir 
        self.listar_report.reverse()

        self.lis_dias = ttk.Treeview(self,
                                       columns = ('Numdia','Namedia','Valuedia','Repor','Code','Apren'))
        self.lis_dias.grid(row=4, column=0, columnspan=4, sticky='nes')

        #scrollbar para la table de repor si exeden los 10 registros 
        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.lis_dias.yview)
        self.scroll.grid(row=4, column=3, sticky='nse')
        self.lis_dias.config(yscrollcommand=self.scroll.set)
        
        

        self.lis_dias.heading('#1', text='NUMDIA')
        self.lis_dias.heading('#2', text='NAMEDIA')
        self.lis_dias.heading('#3', text='VALUEDIA')
        self.lis_dias.heading('#4', text='REPORT')
        self.lis_dias.heading('#5', text='CODE')
        self.lis_dias.heading('#6', text='APREN')

        self.lis_dias.column("#0" ,width = 0)

        

        #Iterar lista report
        for r in self.listar_report:            
            #se evalua si el dia es fin de mes es ese caso se pinta de azul la fila
            dia_fin_de_mes = r[2]
            findia = 'j'

            if dia_fin_de_mes[-2:] == '28':
                findia = 'fin'
            if dia_fin_de_mes[-1:] == '1':
                findia = 'ini'
                #Inser a la table            
            self.lis_dias.insert('',0,text=r[0], tags=(findia), values=(
                r[1], r[2], r[3], r[4],r[5],r[6]
            ))    


            

        self.lis_dias.tag_configure('fin',foreground='black', background='#FF6E33')
        self.lis_dias.tag_configure('ini',foreground='black', background='#357')

#--------------------------ACTION ----------------
#Habilita los campos deacuerdo a la action del User 
    def habilitar_campos(self):
        #Limpiar Campos de texto
       # self.report.set('')
        #self.code.set('')
        #self.apren.set('')
        
        #Entrys
        #self.entry_report.config(state='normal')
        #self.entry_report_code.config(state='normal')
        #self.entry_report_apren.config(state='normal')

        #Botones
        self.buttom_guardar.config(state='normal')
        self.buttom_cancel.config(state='normal')

#Desabilita los campos de acuerdo a la action del User 
    def desabilitar_campos(self):
        self.id_report_lis = None
        #Limpiar Campos de texto
        self.entry_report.delete("1.0",END)
        self.entry_code.delete("1.0",END)
        self.entry_apren.delete("1.0",END)
        self.entry_num.delete("1.0",END)
        
        
        #Entrys
        #self.entry_report.config(state='disabled')
        #self.entry_report_code.config(state='disabled')
        #self.entry_report_apren.config(state='disabled')

        #Bottones        
        
    
#Guardar Datos
    def guardar_datos(self):
               
        #crando el objeto repor
        repor = Report(
            self.dianame,
            self.numdias,   
            self.entry_num.get("1.0",END),
            self.entry_report.get("1.0",END),
            self.entry_code.get("1.0",END),
            self.entry_apren.get("1.0",END),          
            
        )

        if self.id_report_lis == None:
            guardar_report(repor)
        else:
            editar_report(repor, self.id_report_lis)

        self.lis_report()
        self.desabilitar_campos()

        if (self.dianame[-2:] == '28') |  (self.dianame[-1:] == '1'):
            self.report_mes()

#Editar item de la lista de report 
    def editar_report_viw(self):
        self.desabilitar_campos()
        try:
            self.id_report_lis = self.lis_dias.item(self.lis_dias.selection())['text']
            self.report_lis = self.lis_dias.item(self.lis_dias.selection())['values'][3]
            self.code_lis = self.lis_dias.item(self.lis_dias.selection())['values'][4]
            self.activ_lis = self.lis_dias.item(self.lis_dias.selection())['values'][5]
            self.numdi = self.lis_dias.item(self.lis_dias.selection())['values'][2]

            self.habilitar_campos()
            self.entry_report.insert(tk.END,self.report_lis)
            self.entry_code.insert(tk.END, self.code_lis)
            self.entry_apren.insert(tk.END, self.activ_lis)
            self.entry_num.insert(tk.END, self.numdi)


        except:
            title = 'Editar Reporte'
            mesaje = 'Seeccione un repor a editar'
            messagebox.showinfo(title=title, message=mesaje)
            
#Elimiar item de la lista de report
    def eliminar_repor_viw(self):
        try:
            self.id_report_lis = self.lis_dias.item(self.lis_dias.selection())['text']
            eliminar(self.id_report_lis)

            self.lis_report()

            self.id_report_lis = None
            
        except:
            title = 'Eliminar Reporte'
            mesaje = 'Seeccione un repor a Eliminar'
            messagebox.showinfo(title=title, message=mesaje)

    


