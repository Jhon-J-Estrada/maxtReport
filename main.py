#Proyecto Registro de actividades
#__________9-16-31__________

#https://www.youtube.com/watch?v=7QqDQEZ3FTI


import tkinter as tk
from modulos.model_app import Frame


def main():
    root = tk.Tk()
    #para el titulo de la ventana de inicio
    root.title('Report')
    root.geometry('1500x800')
    # se le asigna un icono a la ventana 
    #root.iconbitmap('img/sigma.ico')
    # para modificar el ancho y el alto de la ventana de parte del usuario
    root.readprofile(0,0)#indica q no puede modificar el alto o el ancho

   #barra_menu(root=root)
    #para crear el contenedor de la ventana 
    app = Frame(root = root)
    app.mainloop()

if __name__ == '__main__':
    main()


#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