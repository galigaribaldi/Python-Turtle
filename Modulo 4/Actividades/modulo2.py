import threading
import turtle

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

###Acciones para las tortugas
def forward(turtle, distance,graphics):
    graphics.put((turtle.forward, distance))

def right(turtle, angle, graphics):
    graphics.put((turtle.right, angle))

def left(turtle, angle, graphics):
    graphics.put((turtle.left, angle))
    
def figure(turtle, graphics,num_lados, tam):
    angle = 360/num_lados
    for _ in range(num_lados):
        graphics.put((turtle.left, angle))
        graphics.put((turtle.forward, tam))
def circle(turtle, graphics, tam):
    graphics.put((turtle.circle, tam))

def penup(turtle, graphics):
    graphics.put((turtle.penup,None))

def pendown(turtle, graphics):
    graphics.put((turtle.pendown,None))    
    
def goto(turtle, graphics, posx,posy):
    graphics.put((turtle.goto, (posx, posy)))

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