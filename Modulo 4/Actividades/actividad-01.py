import turtle
from random import *
migue = turtle.Turtle() #inheriting the turtle

migue.penup()
migue.goto(-140,140) #positioning the pen

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


frank = turtle.Turtle() #inheriting the turtle
frank.color('green') #setting the color to green for the first turtle
frank.shape('turtle') #setting the shape to "turtle"
frank.penup() #not ready to draw
frank.goto(-160,100) #positioning the turtle
frank.pendown() #ready todraw


maturin = turtle.Turtle() #inheriting another turtle
maturin.color('red') #setting the color og the turtle to red
maturin.shape('turtle') #declaring the shape of the turtle to "turtle"
maturin.penup() #not ready to draw
maturin.goto(-160,80) #positioning
maturin.pendown() #ready to draw

donatello = turtle.Turtle() #inheriting the last turtle
donatello.color('blue') #setting the color of the turtle as "blue"
donatello.shape('turtle') #declaring the shape of the turtle
donatello.penup() #not ready to draw
donatello.goto(-160,60) #positioning
donatello.pendown() #ready

for turn in range(100): #loop for the racew
    frank.forward(randint(1,5)) #setting the speed randomly with the "random" module
    maturin.forward(randint(1,5)) #setting the speed randomly with the "random" module
    donatello.forward(randint(1,5)) #setting the speed randomly with the "random" module

turtle.done()