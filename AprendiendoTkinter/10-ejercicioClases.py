"""
Calculadora:
    Dos campos de texto
        4 Botones para las operaciones
        Mostrar el resultado de las operaciones
"""
from tkinter import *
from tkinter import messagebox

class Calculadora:
    def __init__ (self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertad = alertas
    
    def sumar(self):
        self.resultado.set(float(self.numero1.get())+ float(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(float(self.numero1.get()) - float(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(float(self.numero1.get()) * float(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        try:
            self.resultado.set(float(self.numero1.get()) / float(self.numero2.get()))
            self.mostrarResultado()
        except ZeroDivisionError:
            messagebox.showerror("Error", "La division entre 0 no existe")
        
    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

calculadora = Calculadora(messagebox)

ventana = Tk()
ventana.title("Ejercicio completo con tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)


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
Entry(marco, textvariable=calculadora.numero1, justify=CENTER).pack()

Label(marco, text = "Segundo Número: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify=CENTER).pack()

Label(marco, text="").pack()

Button(marco, text = "Sumar", command=calculadora.sumar).pack(side=LEFT, fill=X, expand="YES")
Button(marco, text = "Restar", command=calculadora.restar).pack(side=LEFT, fill=X, expand="YES")
Button(marco, text = "Multiplicar", command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand="YES")
Button(marco, text = "Dividir", command=calculadora.dividir).pack(side=LEFT, fill=X, expand="YES")

ventana.mainloop()