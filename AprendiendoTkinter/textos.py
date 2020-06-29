from tkinter import *
ventana = Tk()
ventana.geometry("500x500")
def pruebas(nombre, apellidos, pais):
    return f"Gola {nombre} {apellidos} veo que eres de: {pais}"

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black", # Se pueden pasar en hexadecimal
    padx = 20,
    pady = 20,
    font = ("Consolas", 30)
)
##Empaquetar el texto
texto.pack()
############################################
texto = Label(ventana, text = pruebas("Gali","Garibaldi","Mexico"))
texto.config(
    justify = RIGHT,
    bg="orange",
    font = ("Arial", 18),
    cursor = "clock"
)
##Empaquetar el texto
texto.pack()

ventana.mainloop()