##Creando una tortuga personalizada
import turtle
##Creando una tortuha con nombre
frank = turtle.Turtle()
frank.shape("turtle") ##forma de la tortuga
frank.shapesize(2) ###Tamaño de la fugura
frank.pencolor("green") ###Color de la tortuga
frank.pensize(2) ##Grosor de la tortuga

def cuadrado():
    ##Emepezar a rellenar 
    frank.color("green", "blue") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    for i in range(4):
        frank.fd(100)
        frank.lt(90)
    frank.end_fill() ###fin de relleno
#cuadrado()
def triangulo():
    ##Emepezar a rellenar 
    frank.color("red") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    for i in range(3):
        frank.fd(100)
        frank.lt(120)
    frank.end_fill() ###fin de relleno
triangulo()
input()