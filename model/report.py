from .conexion_bd import ConexionDB
from tkinter import messagebox

def crear_table():
    conexion = ConexionDB()

    sql = ''' 
    CREATE TABLE reportDias(
        id_dia INTEGER,
        numdia INTEGER,
        dianame VARCHAR,
        valuedia VARCHAR,
        report TEXT,
        code TEXT,
        apren TEXT,
        PRIMARY KEY(id_dia AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Crear Table'
        mesaje = 'Se Creo la Base de datos '
        messagebox.showinfo(title=title, message=mesaje)
    except:
        title = 'Crear Table'
        mesaje = 'La Base de datos, Ya existe'
        messagebox.showwarning(title=title, message=mesaje)

def borrar_table():
    conexion = ConexionDB()

    sql = '''
        DROP TABLE reportDias
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Eliminar Table'
        mesaje = 'Se Elimino la Base de datos '
        messagebox.showinfo(title=title, message=mesaje)
    except:
        title = 'Eliminar Table'
        mesaje = 'Ya se elimino la base de datos'
        messagebox.showwarning(title=title, message=mesaje)

class Report:
    def __init__(self, dianame, numdia,valuedia, report, code, apren):
        self.id_report = None
        self.report = report
        self.code = code
        self.apren = apren
        self.numdia = numdia
        self.dianame = dianame
        self.valuedia = valuedia
    

def guardar_report(report):
    conexion = ConexionDB()

    sql = f"""INSERT INTO reportDias(numdia, dianame, valuedia, report, code, apren) VALUES({report.numdia},'{report.dianame}','{report.valuedia}','{report.report}','{report.code}','{report.apren}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title = 'Creando registro '
        mesaje = 'No se guardo registro'
        messagebox.showerror(title=title, message=mesaje)
            
            
def listar_report():
    conexion = ConexionDB()

    lista_report = []
    sql = """ SELECT * FROM reportDias"""

    try:
        conexion.cursor.execute(sql)
        lista_report = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        title = 'Creando registro '
        mesaje = 'La tabla de reporte no existe'
        messagebox.showwarning(title=title, message=mesaje)
    return lista_report

def editar_report(report, id_report):
    conexion = ConexionDB()

    sql = f"""
            UPDATE reportDias SET    
            valuedia = {report.valuedia},      
            report ='{report.report}',
            code ='{report.code}',
            apren ='{report.apren}'
            WHERE id_dia = {id_report}
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Editar Reporte'
        mesaje = 'Se edito el report '
        messagebox.showinfo(title=title, message=mesaje)
    except:
        title = 'Editar Reporte'
        mesaje = f'Error al editar el reporte'
        messagebox.showwarning(title=title, message=mesaje)


def eliminar(id_report):
    conexion = ConexionDB()

    sql = f'DELETE FROM reportDias WHERE id_dia = {id_report}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title = 'Eliminar Reporte'
        mesaje = f'Error al Eliminar el report'
        messagebox.showwarning(title=title, message=mesaje)



