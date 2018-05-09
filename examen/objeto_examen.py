from tkinter import *
class Ventana:
    def __init__(self):
        self.raiz =Tk()
        self.raiz.geometry("300x200")
        self.raiz.title("Ventana principal")
        self.raiz.configure(bg="beige")
        ###Declaracion de botones
        boton_salir = Button(self.raiz, text = "Salir", command = self.raiz.destroy)
        boton_2 = Button(self.raiz, text = "Boton")
        boton_3 = Button(self.raiz, text = "Circulo")
        ###posicionamiento
        boton_salir.pack()
        boton_2.pack()
        boton_3.pack()
    def Circulo(self):
        self.mandalas = Toplevel()
        self.mandalas.geometry("600x600")
        self.mandalas.resizable(0,0)
        self.mandalas.title("Circulo")
        

def main():
    aplicacion = Ventana()
    return 0

if __name__  == "__main__":
    main()
