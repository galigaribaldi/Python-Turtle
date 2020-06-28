from tkinter import *

class Ventana(object):
	def __init__(self):
		self.raiz =Tk()
		self.raiz.geometry("300x200")
		self.raiz.title("Ventana principal")
		boton = Button(self.raiz, text ="Abrir", command = self.abrir)
		boton.pack(side = BOTTOM)
		self.raiz.mainloop()
	
	def abrir(self):
		self.dialogo = Toplevel()
		self.dialogo.geometry("300x300")
		self.dialogo.resizable(0,0)
		self.dialogo.title("ventana 2")
		boton = Button(self.dialogo, text = "Cerrar", command = self.dialogo.destroy)
		boton.pack(side=BOTTOM)




def main():
	aplicacion = Ventana()
	return 0

if __name__  == "__main__":
	main()