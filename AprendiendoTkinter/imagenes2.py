from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("600x500")
Label(ventana, text="Texto").pack()

imagen = Image.open("Imagenes/Prueba.png")
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=W)
ventana.mainloop()