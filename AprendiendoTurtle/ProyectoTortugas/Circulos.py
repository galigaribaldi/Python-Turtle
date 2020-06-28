from turtle import *

def circulo(color):
	rt(90)
	pencolor(str(color))
	circle(60,360)
	fd(50)
	lt(10)
	fd(50)
	lt(10)

def generador(tamano, color1, color2, desplaza):	
	for i in range(int(tamano)):
		circulo(color1)
		circulo(color2)
		circulo(color1)
		circulo(color2)
	pu()
	home()
	fd(desplaza)
	pd()

def Circulos():
	#tracer(0,0)
	bgcolor("black")
	generador(10, "green", "blue", -400)
	generador(10, "red", "lightgreen", 500)
	generador(10, "white", "yellow",0)	
	#update()
