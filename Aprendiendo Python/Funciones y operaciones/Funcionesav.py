from turtle import *
from time import *
def cuadrado():
	shape("turtle")
	color("green")
	begin_fill()
	pencolor("green")
	pensize(9)
	forward(200)
	rt(90)
	forward(200)
	rt(90)
	forward(200)
	rt(90)
	forward(200)
	rt(90)
	end_fill()
	sleep(3)
def triangulo():
	shape("triangle")
	shapesize(outline=8)
	for i in range(3):
		fd(100)
		rt(120)
triangulo()


