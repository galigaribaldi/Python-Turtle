from turtle import *
from time import *
speed(0)
def Circulos():
	color("green")
	begin_fill()
	for i in range(50):
		circle(5*i)
		circle(-5*i)
		left(i)
	end_fill()

def Figuras(tam, lados, giros):
	for i in range(lados):
		forward(tam)
		left((int(giros)))
	exitonclick()

##Triangulo, pentagono y hexagono
def Ran():
	for i in range(30):
		Figuras(i*100, 5, 360/5)
		left(i)
	exitonclick()
#Figuras(100, 4, 90)
#Ran()
Circulos()
