#### Basico sin usar funciones
from turtle import *

###Dividir 360/numero de lados que queremos obtener de la figura a trazar
###360/4 = 90
def cuadrado():    
    shape("turtle")
    #pencolor("red")
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
#cuadrado()
###Dividir 360/numero de lados que queremos obtener de la figura a trazar
###360/3 = 120
def triangulo():    
    shape("turtle")
    #pencolor("red")
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
triangulo()
input()