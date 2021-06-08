import queue
import threading
###
#from modulo2 import forward,right, left, figuree, process_queue, generate_screen,generate_Tortugas
from modulo2 import *
def func1():
    penup(frank,graphics)
    goto(frank,graphics,-300, 200)
    pendown(frank,graphics)
    for _ in range(4):
        right(frank, 45,graphics)
        forward(frank, 40,graphics)
        left(frank, 45,graphics)
        forward(frank, 30,graphics)
        left(frank, 45,graphics)
        forward(frank, 40,graphics)
        right(frank, 45,graphics)
        forward(frank, 30,graphics)

def func2():
    penup(maturin,graphics)
    goto(maturin,graphics,-300, 180)
    pendown(maturin,graphics)
    for _ in range(4):
        left(maturin, 45,graphics)
        forward(maturin, 40,graphics)
        right(maturin, 45,graphics)
        forward(maturin, 30,graphics)
        right(maturin, 45,graphics)
        forward(maturin, 40,graphics)
        left(maturin, 45,graphics)
        forward(maturin, 30,graphics)
def func3():
    penup(maturin,graphics)
    goto(maturin,graphics,-300, 180)
    pendown(maturin,graphics)
    for _ in range(4):
        figure(maturin, graphics,4, 20)
        forward(maturin, 40,graphics)
        circle(maturin, graphics,4)


###Queue de Reproduccion
graphics = queue.Queue(1)  # size = number of hardware threads you have - 1
###Tortuga 1
frank = generate_Tortugas("blue","turtle",1,0) ##Primera Tortuga
###Tortuga 2
maturin = generate_Tortugas("red","arrow",1,3) ##Segunda tortuga
###Hilos de Ejecución
threading.Thread(target=func1).start()
threading.Thread(target=func3).start()

screen = generate_screen("")

process_queue(graphics, screen)

screen.exitonclick()
