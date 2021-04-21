import turtle
##COLORES: https://trinket.io/docs/colors
###Escenario
screen = turtle.Screen()
screen.bgcolor('black')
##Tortuga 1
frank = turtle.Turtle()
colors =['orange', 'red', 'pink', 'yellow', 'blue', 'green']
frank.pen(speed=25)#setting the speed of the pen to 25
frank.shape('turtle')#setting the shape of the turtle as "classic

##Tortuga 2
frank2 = turtle.Turtle()
colors2 =['dark turquoise', 'turquoise', 'medium spring green', 'yellow', 'blue', 'green']
frank2.pen(speed=25)#setting the speed of the pen to 25
frank2.shape('turtle')#setting the shape of the turtle as "classic

##Tortuga 3
frank3 = turtle.Turtle()
colors3 =['orange red', 'light salmon', 'bisque', 'yellow', 'blue', 'green']
frank3.pen(speed=25)#setting the speed of the pen to 25
frank3.shape('turtle')#setting the shape of the turtle as "classic

def spiral_shape(name_turtle,p,c, colors):
    if p > 0:
        name_turtle.forward(p)
        name_turtle.right(c)
        name_turtle.pencolor(colors[p%6])
        spiral_shape(name_turtle,p-5,c, colors)
###Tortuga 1
frank.setpos(-300, 0)#setting the position as given
spiral_shape(frank,400, 121, colors)#calling the function with the given arguments
###Tortuga 2
frank2.setpos(-600,0)
spiral_shape(frank2,400, 121, colors2)#calling the function with the given arguments
###Tortuga 3
frank3.setpos(0,100)
spiral_shape(frank3,400, 121, colors3)#calling the function with the given arguments
screen.exitonclick()