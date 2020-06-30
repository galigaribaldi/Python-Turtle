from tkinter import *
from tkinter import messagebox as MessageBox
ventana = Tk()
ventana.config(bd=70)
def sacar_alerta():
    MessageBox.showinfo("Alerta!!", "Es una alerta")
    MessageBox.showerror("Alerta!!", "Es una alerta")
    MessageBox.showwarning("Alerta!!", "Es una alerta")

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres continuar?")
    if resultado != "yes":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()
        
    
Button(ventana, text="Mostrar Alerta", command=sacar_alerta).pack()
###Qye no se ejecute la funcion automarticamente
Button(ventana, text="Salir", command=lambda: salir("Funcion")).pack()

ventana.mainloop()