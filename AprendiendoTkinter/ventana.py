from tkinter import *
import os.path

##Crear una ventana Raiz
ventana = Tk()
##Comprobar si existe un archivo
ruta_icono=os.path.abspath("Imagenes/pyi.ico")
##Mostrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()
##Icono de la ventana
ventana.iconbitmap(ruta_icono)
##Titulo de la ventana
ventana.title("Interfaz Gráfica con Tkinter")
##Cambio al tamaño de la ventana
ventana.geometry("750x450")

##Bloqueo de tamaño de la ventana
ventana.resizable(0,0)

#Mostrar la ventana (Debe ser el ultimo elemento)
ventana.mainloop()