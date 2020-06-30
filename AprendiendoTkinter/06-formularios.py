from tkinter import *
ventana =Tk()
ventana.title("Formularios Python")
ventana.geometry("700x400")
##Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0,columnspan=3,sticky=E)
##Label para erl campo
label = Label(ventana, text = "Nombre")
label.grid(row=1, column=0, sticky=W,padx=5, pady=5)

#Campo Texto (Nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=S)
#campo_texto.config(justify="RIGHT", state="NORMAL")

############Apellidos
##Label para erl campo
label = Label(ventana, text = "Aepllidos")
label.grid(row=2, column=0, sticky=W,padx=5, pady=5)

#Campo Texto 
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky=S)

##Label para erl campo Descripcion
label = Label(ventana, text = "DEscripcion")
label.grid(row=3, column=0, sticky=N,padx=5, pady=5)

###Campo de texto para decripcion
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(width=30, height=5, font=("Arial", 13), padx=15,pady=15)

##Boton
Label(ventana).grid(row=4,column=1)
boton = Button(ventana, text = "Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=15, pady=15, bg="Green", fg="white")
ventana.mainloop()