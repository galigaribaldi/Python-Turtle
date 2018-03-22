###Ciclos de repeticion
from turtle import *

shape("turtle")

def cuadrado():
	color("blue", "red")
	begin_fill()
	pensize(4)
	for i in range(4):
		fd(100) ###abreviaciones de el comando forward
		lt(90)  ###Abreviaciones del comando left
	end_fill()

def triangulo():
	color("green", "black")
	pensize(3)
	begin_fill()
	for i in range(3):
		fd(100)
		lt(120)
	end_fill()

def pentagono():
	color("purple", "green")
	pensize(3)
	begin_fill()
	for i in range(5):
		fd(100)
		lt(360/5)
	end_fill()

cuadrado()
triangulo()
pentagono()

