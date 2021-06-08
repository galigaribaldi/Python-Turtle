import turtle
from random import *
##Generación de Tortugas
##Migue = Tortuga de pista
migue = turtle.Turtle() ##Primera Tortuga
migue.penup()
##Frank = Tortuga competidora 1
frank = turtle.Turtle()
frank.color('green') 
frank.shape('turtle') 
##MAturin = Tortuga competidora 2
maturin = turtle.Turtle()
maturin.color('red')
maturin.shape('turtle')
###donatello = Tortuga competidora 3
donatello = turtle.Turtle()
donatello.color('blue')
donatello.shape('turtle')

###Acciones
migue.goto(-140,140) #Tortuga dibujadora
##Competidor 1
frank.penup()
frank.goto(-160,100)
frank.pendown()
##Competidor 2
maturin.penup()
maturin.goto(-160,80)
maturin.pendown()
##Competidor 3
donatello.penup()
donatello.goto(-160,60)
donatello.pendown()
###Pista
for sp in range(15): #loop for creating the lines labelled with numbers
    migue.speed(10)#setting the speed
    migue.write(sp)#writing the int
    migue.right(90)#setting right at 90 degrees
    migue.forward(10)#forward at 10 units
    migue.pendown()#ready to draw
    migue.forward(150)#forward at 150 units
    migue.penup()#not ready to draw
    migue.backward(160)#back at 160 units
    migue.left(90)#left set at 90 degrees
    migue.forward(20)#forward at 20 units

###Competidores
for turn in range(100): #loop for the racew
    frank.forward(randint(1,5)) #setting the speed randomly with the "random" module
    maturin.forward(randint(1,5)) #setting the speed randomly with the "random" module
    donatello.forward(randint(1,5)) #setting the speed randomly with the "random" module

turtle.done()