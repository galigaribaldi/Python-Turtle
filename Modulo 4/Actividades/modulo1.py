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
##Acciones
def figura(tam, num_lados, tortuga, color1,color2):
    tortuga.color(color1,color2)
    tortuga.begin_fill()
    for i in range(num_lados):
        tortuga.fd(tam)
        tortuga.lt(360/num_lados)
    tortuga.end_fill()
def circle(tam, tortuga, color1,color2):
    tortuga.color(color1,color2)
    tortuga.begin_fill()
    tortuga.circle(tam)
    tortuga.end_fill()    
        