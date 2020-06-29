from tkinter import *
class Ventana:
	def __init__(self):
		self.raiz = Tk()
		self.raiz.geometry("500x500")
		self.raiz.title("Imagenes")
		self.raiz.configure(bg="beige")
		boton_salir = Button(self.raiz, text = "Salir", command = self.raiz.destroy)
		boton_Imagenes = Button(self.raiz, text ="Imagenes", command = self.imagenes)		
		boton_salir.pack()
		boton_Imagenes.pack()
		self.raiz.mainloop()

	def imagenes(self):
		self.imagenes = Toplevel()
		self.imagenes.geometry("800x800")
		self.imagenes.resizable(0,0)
		self.imagenes.title("Serpiente")
		##DEfinir una imagen
		imagen = PhotoImage(file="img/HTML5_Logo_512.png")
		fondo = Label(self.imagenes, image = imagen)
		fondo.pack() 	


def main():
	aplicacion = Ventana()
	return 0

if __name__  == "__main__":
	main()