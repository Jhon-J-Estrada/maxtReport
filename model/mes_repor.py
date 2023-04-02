from .conexion_bd import ConexionDB
from tkinter import messagebox

def crear_table_mes():
    conexion = ConexionDB()

    sql = ''' 
    CREATE TABLE mesRepor(
        id_mes INTEGER,
        nummes INTEGER,
        mesname VARCHAR,
        valuemes VARCHAR,
        odjet TEXT,         
        apren TEXT,
        PRIMARY KEY(id_mes AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Crear Table'
        mesaje = 'Se Creo la Table Repor Meses'
        messagebox.showinfo(title=title, message=mesaje)
    except:
        title = 'Crear Error '
        mesaje = 'Error al crear la Tabla'
        messagebox.showwarning(title=title, message=mesaje)

def borrar_table_mes():
    conexion = ConexionDB()

    sql = '''
        DROP TABLE mesRepor
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Eliminar Table'
        mesaje = 'Se Elimino la tabla reporte por mes  '
        messagebox.showinfo(title=title, message=mesaje)
    except:
        title = 'Eliminar Table'
        mesaje = 'Ya se elimino la tabla report mes '
        messagebox.showwarning(title=title, message=mesaje)

class Report_mes:
    def __init__(self, nummes,mesname,valuemes, odjet,  apren):
        self.id_report = None
        self.odjet = odjet        
        self.apren = apren
        self.nummes = nummes
        self.mesname = mesname
        self.valuemes = valuemes
    

def guardar_report_mes(report):
    conexion = ConexionDB()

    sql = f"""INSERT INTO mesRepor(nummes, mesname, valuemes, odjet,apren) VALUES({report.nummes},'{report.mesname}','{report.valuemes}','{report.odjet}','{report.apren}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title = 'Creando registro '
        mesaje = 'No se guardo registro'
        messagebox.showerror(title=title, message=mesaje)
            
            
def listar_report_mes():
    conexion = ConexionDB()

    lista_report = []
    sql = """ SELECT * FROM mesRepor"""

    try:
        conexion.cursor.execute(sql)
        lista_report = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        title = 'Creando registro '
        mesaje = 'La tabla de reporte no existe'
        messagebox.showwarning(title=title, message=mesaje)
    return lista_report

def editar_report_mes(report, id_report):
    conexion = ConexionDB()

    sql = f"""
            UPDATE mesRepor SET    
            valuemes = '{report.valuemes}',      
            odjet ='{report.odjet}',            
            apren ='{report.apren}'
            WHERE id_mes = {id_report}
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Editar Reporte'
        mesaje = 'Se edito el report '
        #messagebox.showinfo(title=title, message=mesaje)
    except:
        title = 'Editar Reporte'
        mesaje = 'Error al editar el reporte del mes'
        messagebox.showwarning(title=title, message=mesaje)


def eliminar_mes(id_report):
    conexion = ConexionDB()

    sql = f'DELETE FROM mesRepor WHERE id_mes = {id_report}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title = 'Eliminar Reporte'
        mesaje = f'Error al Eliminar el report Mes'
        #messagebox.showwarning(title=title, message=mesaje)



