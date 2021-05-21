import turtle
##Pantalla
ws = turtle.Screen()
#ws.bgcolor("black")
ws.title("Sharingan")
ws.setup(width=900, height=900) #geometry of the GUI
##Tortuga
frank = turtle.Turtle()
frank.speed(0)
frank.shape("turtle")
def circulo_interno(tam):
    frank.rt(180) 
    frank.begin_fill()
    frank.circle(tam)
    frank.end_fill()    
    frank.rt(70)
    ###
    if tam > 50:
        frank.pensize(30)
    else:
        frank.pensize(10)
    frank.circle(tam-5,100)
    frank.penup()
    frank.circle(tam-5,260)
    frank.lt(90)
    frank.fd(tam/3)
    frank.rt(90)
    frank.pendown()
    frank.circle(tam,80)
    frank.penup()
    frank.circle(tam,280)
    frank.pendown()
    frank.pensize(1)
    frank.rt(110)

def triangulo(tam):
    for _ in range(3):
        frank.lt(360/3)
        frank.penup()
        frank.forward(tam)
        frank.pendown()
        frank.color("black","black")
        frank.begin_fill()
        circulo_interno(20)
        frank.end_fill()
#input()
###Circulo exterior
frank.pensize(10)
frank.color("black","red")
frank.begin_fill()
frank.penup()
frank.goto(10,-210)
frank.pendown()
frank.circle(300)
frank.end_fill()
#####
frank.penup()
frank.goto(150,0)
frank.pendown()
triangulo(300)
####Cicrulo de en medio
frank.penup()
frank.goto(0,70)
frank.pendown()
frank.color("black","black")
frank.begin_fill()
frank.circle(40)
frank.end_fill()
####Cicrulo de en medio
frank.penup()
frank.goto(5,-90)
frank.pendown()
frank.color("black")
frank.pensize(5)
frank.circle(180)
#####
turtle.done()