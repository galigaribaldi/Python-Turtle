import turtle
colors =['orange', 'red', 'pink', 'yellow', 'blue', 'green']

screen = turtle.Screen()
frank = turtle.Turtle()
frank.speed(0)
screen.bgcolor('black')

for x in range(360):
    frank.pencolor(colors[x%6])
    print(x%6)
    frank.width(x/(5+1))
    frank.fd(x)
    frank.lt(20)
    