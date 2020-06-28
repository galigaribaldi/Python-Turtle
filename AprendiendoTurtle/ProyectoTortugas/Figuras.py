###Ciclos de repeticion
from turtle import *

shape("turtle")
pencolor("black")
bgcolor("white")
def cuadrado():
	for i in range(4):
		fd(100) ###abreviaciones de el comando forward
		lt(90)  ###Abreviaciones del comando left


def triangulo():
	for i in range(3):
		fd(100)
		lt(120)

def pentagono():
	for i in range(5):
		fd(100)
		lt(360/5)

def hexagono():
	for i in range(6):
		fd(100)
		lt(360/6)

def Circulo():
	circle(100)

