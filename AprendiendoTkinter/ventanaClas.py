from tkinter import *
import os.path

class Prorgrama:
    def __init__(self):
        ##Titulo de la ventana
        self.title= "Interfaz Gráfica con Tkinter"
        self.icon = "Imagenes/pyi.ico"
        self.size = "750x450"
        self.resizable = False
        
    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)
        ruta_icono=os.path.abspath(self.icon)
        ventana.iconbitmap(ruta_icono)
        ##Cambio al tamaño de la ventana
        ventana.geometry(self.size)
        if self.resizable == True:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
            
    def addtexto(self, dato):
        texto = Label(self.ventana, text =dato)
        texto.pack()
        
    def mostrar(self):
        self.ventana.mainloop()
        
programa = Prorgrama()
programa.cargar()
programa.addtexto("Texto 2")
programa.addtexto("Texto 3")
programa.addtexto("Texto 4")
programa.addtexto("Texto 5")
programa.mostrar()