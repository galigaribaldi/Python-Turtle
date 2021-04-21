##Creando una tortuga personalizada
import turtle
##Creando una tortuha con nombre
frank = turtle.Turtle()
frank.shape("turtle") ##forma de la tortuga
frank.shapesize(2) ###Tamaño de la fugura
frank.pencolor("green") ###Color de la tortuga
frank.pensize(2) ##Grosor de la tortuga

def figura(numero_lados, tam):
    ##Emepezar a rellenar 
    frank.color("green", "blue") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    for i in range(numero_lados):
        frank.fd(tam)
        frank.lt(360/numero_lados)
    frank.end_fill() ###fin de relleno
figura(4,100)
frank.forward(100)
figura(5,100)