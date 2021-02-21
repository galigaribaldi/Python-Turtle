from turtle import *
from time import *
bgcolor("white")
def Circulos():
	for i in range(50):
		circle(5*i)
		circle(-5*i)
		left(i)

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
