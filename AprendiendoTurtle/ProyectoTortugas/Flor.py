from turtle import *
from time import *
pencolor("black")
bgcolor("white")
def Cuadrado():
	for i in range(4):
		fd(100)
		lt(90)

def Triangullo():
	for i in range(3):
		fd(100)
		lt(120)

def F1():
	for i in range(10):
		Cuadrado()
		lt(360/10)

def F2():
	for i in range(10):
		Triangullo()
		lt(360/10)

def Flor():
	F1()
	j=0
	for i in range(4):
		j=j+90
		home()
		lt(j)
		fd(200)
		F2()

def circulo():
	for i in range(360):
		lt(1)
		fd(1)




