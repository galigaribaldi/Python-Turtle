##Librerias necesarias
from tkinter import *
from Figuras import *
##Modulos propios
from turtle import *
from Comandos import *
from Mandala import *
from Flor import *
from Circulos import *
class Menu():
	def __init__(self):
		speed(0)
		self.raiz =Tk()
		self.raiz.geometry("300x200")
		self.raiz.title("Ventana principal")
		self.raiz.configure(bg="beige")
		###Declaracion de botones
		boton_salir = Button(self.raiz, text = "Salir", command = self.raiz.destroy)
		boton_Mandalas = Button(self.raiz, text ="Mandalas", command = self.mandalas)
		boton_Figuras = Button(self.raiz, text ="Figuras", command = self.figuras)
		boton_Comandos = Button(self.raiz, text ="Comandos", command = self.comandos)
		boton_limpiar = Button(self.raiz, text = "Limpiar Pantalla", command = LimpiarPantalla)		
		###posicionamiento
		boton_Mandalas.pack()
		boton_Figuras.pack()
		boton_Comandos.pack()
		boton_limpiar.pack()
		boton_salir.pack()
		self.raiz.mainloop()
	
	def figuras(self):
		###Configuracion inicial
		self.figuras = Toplevel()
		self.figuras.geometry("300x300")
		self.figuras.resizable(0,0)
		self.figuras.title("Figuras")
		##Botones
		boton_salir = Button(self.figuras, text = "Cerrar", command = self.figuras.destroy)
		boton_Cuadrado = Button(self.figuras, text = "Cuadrado", command = cuadrado)
		boton_Triangulo = Button(self.figuras, text = "Triangulo", command = triangulo)		
		boton_Hexagono = Button(self.figuras, text = "Hexagono", command = hexagono)
		boton_Pentagono = Button(self.figuras, text = "Pentagono", command = pentagono)
		boton_limpiar = Button(self.figuras, text = "Limpiar Pantalla", command = LimpiarPantalla)		
		###posocionamiento
		boton_Cuadrado.pack()
		boton_Triangulo.pack()
		boton_Hexagono.pack()
		boton_Pentagono.pack()
		boton_limpiar.pack()
		boton_salir.pack(side=BOTTOM)

	def comandos(self):
		self.comandos = Toplevel()
		self.comandos.geometry("300x300")
		self.comandos.resizable(0,0)
		self.comandos.title("Comandos")
		###Botones
		boton = Button(self.comandos, text = "Cerrar", command = self.comandos.destroy)
		boton_Avanza = Button(self.comandos, text = "Avanza", command = Avanza)
		boton_Gira_derecha = Button(self.comandos, text = "Gira_derecha", command =Gira_Derecha)
		boton_Gira_Izquierda = Button(self.comandos, text = "Gira_Izquierda", command = Gira_Izquierda)
		boton_limpiar = Button(self.comandos, text = "Limpiar Pantalla", command = LimpiarPantalla)				
		##posicionamiento
		boton.pack(side=BOTTOM)
		boton_Gira_Izquierda.pack()
		boton_Gira_derecha.pack()
		boton_Avanza.pack()
		boton_limpiar.pack()

	def mandalas(self):
		self.mandalas = Toplevel(); self.mandalas.geometry("300x300")
		self.mandalas.resizable(0,0)
		self.mandalas.title("Mandalas")
		###Botones
		boton = Button(self.mandalas, text = "Cerrar", command = self.mandalas.destroy)
		boton_1 = Button(self.mandalas, text = "Mandala 1", command = Circulos)
		boton_2 = Button(self.mandalas, text = "Mandala 2", command = Ran)
		boton_3 = Button(self.mandalas, text = "Mandala 3", command = Flor)		
		#boton_4 = Button(self.mandalas, text = "Mandala 3", command = )		
		boton_limpiar = Button(self.mandalas, text = "Limpiar Pantalla", command = LimpiarPantalla)		
		##posicionamiento
		boton_1.pack()
		boton_2.pack()
		boton_3.pack()
		#boton_4.pack()
		boton_limpiar.pack()
		boton.pack(side=BOTTOM)

def main():
	aplicacion = Menu()
	return 0

if __name__  == "__main__":
	main()