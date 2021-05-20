import turtle

frank = turtle.Turtle()
frank.speed(0)
def cuadrado(tam):
    for _ in range(4):
        frank.forward(tam)
        frank.right(90)   

def exterior(tam):
    listaletras = ["A", "B", "C", "D", "E", "F", "G", "H"]
    listaletras.reverse()
    listanumeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
    frank.penup()
    frank.goto(-270,318)
    frank.pendown()
    frank.pensize(7)
    for _ in range(2):
        for i in listaletras:
            frank.forward(tam)
            frank.write(i,font=("Arial", 20),align="center")
        frank.right(90)
        for i in listanumeros:
            frank.forward(tam)
            frank.write(i,font=("Arial", 20),align="right")
        frank.right(90)
        

def hilera_horizontal(tam,opcion):
    color1=["black", "white"]
    color2=["white", "black"]
    lista= color2
    if opcion==1:
        lista = color1
    for i in range(4):
        ##Cuadro 1
        frank.color("black",lista[0])
        frank.begin_fill()
        cuadrado(tam)
        frank.fd(tam)
        frank.end_fill()
        ##Cuadro 2
        frank.color("black", lista[1])
        frank.begin_fill()
        cuadrado(tam)
        frank.fd(tam)
        frank.end_fill()        

def tablero(tam):
    frank.penup()
    frank.goto(-250,300)
    frank.pendown()
    for i in range(1,9):
        op = 0
        if i%2==0:
            op=1
        hilera_horizontal(tam,op)
        frank.penup()
        frank.rt(90)
        frank.fd(tam)
        frank.rt(90)
        frank.fd(tam*8)
        frank.lt(180)
        frank.pendown()

def main(tam1, tam2):
    #input()
    ##Dibujar el tablero
    tablero(tam1)
    ###Lineas de afuera 
    exterior(tam2)
    turtle.done()
main(70,75)