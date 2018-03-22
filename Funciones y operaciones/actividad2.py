from turtle import *
def triangulo():
	shape("triangle")
	shapesize(outline=8)
	color("purple")
	begin_fill()
	pencolor("gold")
	for i in range (3):
		fd(100)
		rt(120)
	end_fill()
triangulo()

def poligono():
	forwad(100)
	left(360/6)
    forwad(100)
	left(360/6)
    forwad(100)
	left(360/6)
    forwad(100)
	left(360/6)
	forwad(100)
	left(360/6)

poligono()









