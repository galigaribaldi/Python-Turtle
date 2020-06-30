"""
Calculadora:
    Dos campos de texto
        4 Botones para las operaciones
        Mostrar el resultado de las operaciones
"""
from tkinter import *
from tkinter import messagebox
ventana = Tk()
ventana.title("Ejercicio completo con tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

def sumar():
    resultado.set(float(numero1.get())+ float(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(float(numero1.get()) - float(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(float(numero1.get()) * float(numero2.get()))
    mostrarResultado()

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except ZeroDivisionError:
        messagebox.showerror("Error", "La division entre 0 no existe")
    
def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

marco = Frame(ventana, width=310, height=200)
marco.config(
    bd=5,
    padx=15,
    pady=15,
    relief = SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text = "Primer Número: ").pack()
Entry(marco, textvariable=numero1, justify=CENTER).pack()

Label(marco, text = "Segundo Número: ").pack()
Entry(marco, textvariable=numero2, justify=CENTER).pack()

Label(marco, text="").pack()

Button(marco, text = "Sumar", command=sumar).pack(side=LEFT, fill=X, expand="YES")
Button(marco, text = "Restar", command=restar).pack(side=LEFT, fill=X, expand="YES")
Button(marco, text = "Multiplicar", command=multiplicar).pack(side=LEFT, fill=X, expand="YES")
Button(marco, text = "Dividir", command=dividir).pack(side=LEFT, fill=X, expand="YES")

ventana.mainloop()