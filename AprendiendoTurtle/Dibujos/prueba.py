from turtle import *
from time import *

speed(0)
def Cuadrado():
	shape("turtle")
	pencolor("red")
	for i in range(4):
		fd(100)
		lt(90)

def Triangullo():
	pencolor("green")
	for i in range(3):
		fd(100)
		lt(120)

def F1():
	begin_fill()
	for i in range(10):
		Cuadrado()
		lt(360/10)
	end_fill()
	sleep(3)

def F2():
	begin_fill()
	for i in range(10):
		Triangullo()
		lt(360/10)
	end_fill()
	sleep(3)	
def Flor():
	speed(3)
	F1()
	j=0
	for i in range(4):
		j=j+90
		home()
		lt(j)
		fd(200)
		F2()
	sleep(5)

def circulo():
	for i in range(360):
		lt(1)
		fd(1)

Flor()



