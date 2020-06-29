from tkinter import *
ventana = Tk()
#ventana.geometry("500x500")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black", # Se pueden pasar en hexadecimal
    padx = 20,
    pady = 20,
    font = ("Consolas", 20)
)
##Empaquetar el texto
texto.pack(side=TOP, fill=X, expand=YES)
############################################
texto = Label(ventana, text = "Basico 1")
texto.config(
    height = 3,
    bg="red",
    font = ("Arial", 18),
    padx=10,
    pady=20,
    cursor = "clock"
)
##Empaquetar el texto
texto.pack(side=LEFT, fill=X, expand=YES)
###########################################
texto = Label(ventana, text = "Basico 2")
texto.config(
    height = 3,
    bg="Green",
    font = ("Arial", 18),
    padx=10,
    pady=20,
    cursor = "clock"
)
##Empaquetar el texto
texto.pack(side=LEFT, fill=X, expand=YES)
##############################################
texto = Label(ventana, text = "Basico 3")
texto.config(
    height = 3,
    bg="Blue",
    font = ("Arial", 18),
    padx=10,
    pady=20,
    cursor = "clock"
)
##Empaquetar el texto
texto.pack(anchor=NW)
ventana.mainloop()