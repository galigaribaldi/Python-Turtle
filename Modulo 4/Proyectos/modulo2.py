import threading
import turtle
from time import sleep
###Generador de Pantallas
def generate_screen(color):
    sc = turtle.Screen()
    if color != "":
        sc.bgcolor(color)
    return sc
##Tortugas
def generate_Tortugas(color, forma, tamaño, velocidad):
    nombre = turtle.Turtle()
    nombre.speed(velocidad)
    nombre.color(color)
    nombre.shape(forma)
    nombre.shapesize(tamaño)
    return nombre
###Atributos de color: IMPORTANTE: Solo recibe 1 color como maximo
def color(turtle, graphics, color):
    graphics.put((turtle.color, color))
###Color de la pluma
def pencolor(turtle, graphics, color):
    graphics.put((turtle.pencolor, color))
###Tamaño de la pluma
def pensize(turtle, graphics, tam):
    graphics.put((turtle.pensize, tam))
###Atributos de relleno
def fillcolor(turtle, graphics, color):
    graphics.put((turtle.fillcolor, color))
###Iniciar relleno
def begin_fill(turtle, graphics):
    graphics.put((turtle.begin_fill, None))
###Finalizar relleno
def end_fill(turtle, graphics):
    graphics.put((turtle.end_fill, None))        

###Acciones para las tortugas
##Avanzar
def forward(turtle, distance,graphics):
    graphics.put((turtle.forward, distance))
##Derecha
def right(turtle, angle, graphics):
    graphics.put((turtle.right, angle))
##Izquierda
def left(turtle, angle, graphics):
    graphics.put((turtle.left, angle))
##Figura    
def figure(turtle, graphics,num_lados, tam):#
    angle = 360/num_lados
    for _ in range(num_lados):
        graphics.put((turtle.left, angle))
        graphics.put((turtle.forward, tam))

##Creacion de Circulo            
def circle(turtle, graphics, tam):#
    graphics.put((turtle.circle, tam))
##Alzar pluma
def penup(turtle, graphics):
    graphics.put((turtle.penup,None))
##Bajar pluma
def pendown(turtle, graphics):
    graphics.put((turtle.pendown,None))    
##Ir a posicion
def goto(turtle, graphics, posx,posy):
    graphics.put((turtle.goto, (posx, posy)))
##Write
def write(turtle, graphics,texto):
    graphics.put((turtle.write, texto))    
##Backward
def backward(turtle, graphics,tam):
    graphics.put((turtle.backward, tam))        
###Procesos en cola para la tortuga
def process_queue(graphics,screen):
    while not graphics.empty():
        graphic, argument = graphics.get()
        if argument:
            graphic(argument)
        else:
           graphic()
    if threading.active_count() > 1:
        screen.ontimer(process_queue, 100)