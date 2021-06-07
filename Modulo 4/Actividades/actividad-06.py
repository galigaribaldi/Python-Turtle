import queue
import threading
###
#from modulo2 import forward,right, left, figuree, process_queue, generate_screen,generate_Tortugas
from modulo2 import *
##torttuga 1
frank = generate_Tortugas("green", "turtle", 1, 0)
##tortuga 2
maturin = generate_Tortugas("yellow", "arrow", 1, 0)

##torttuga 3
frank0 = generate_Tortugas("blue", "turtle", 1, 0)
##tortuga 4
maturin0 = generate_Tortugas("red", "arrow", 1, 0)

##torttuga 5
frank1 = generate_Tortugas("blue violet", "turtle", 1, 0)
##tortuga 6
maturin1 = generate_Tortugas("linen", "arrow", 1, 0)

##torttuga 7
frank2 = generate_Tortugas("deep pink", "turtle", 1, 0)
##tortuga 8
maturin2 = generate_Tortugas("dark cyan", "arrow", 1, 0)
##torttuga 9
frank3 = generate_Tortugas("medium slate blue", "turtle", 1, 0)
##tortuga 10
maturin3 = generate_Tortugas("white", "arrow", 1, 0)

###Queue de Reproduccion
graphics = queue.Queue(1)  # size = number of hardware threads you have - 1
#####################################################
##MAturin Circulo interno
def func1():
    for i in range(30):
        figure(maturin, graphics,3,70)
        right(maturin, 65, graphics)
##Frank circulo externo
def func2():
    for i in range(60):
        figure(frank, graphics,8,100)
        right(frank, 91,graphics)    
#####################################################          
##MAturin Circulo interno
def func3():
    penup(maturin0,graphics)
    goto(maturin0,graphics,-300, 180)
    pendown(maturin0,graphics)
    for i in range(30):
        figure(maturin0, graphics,3,70)
        right(maturin0, 65, graphics)
##Frank circulo externo
def func4():
    penup(frank0,graphics)
    goto(frank0,graphics,-300, 180)
    pendown(frank0,graphics)    
    for i in range(60):
        figure(frank0, graphics,8,100)
        right(frank0, 91,graphics)    

#####################################################          
##MAturin Circulo interno
def func5():
    penup(maturin1,graphics)
    goto(maturin1,graphics,300, 180)
    pendown(maturin1,graphics)
    for i in range(30):
        figure(maturin1, graphics,3,70)
        right(maturin1, 65, graphics)
##Frank circulo externo
def func6():
    penup(frank1,graphics)
    goto(frank1,graphics,300, 180)
    pendown(frank1,graphics)    
    for i in range(60):
        figure(frank1, graphics,8,100)
        right(frank1, 91,graphics)         
        
#####################################################          
##MAturin Circulo interno
def func7():
    penup(maturin2,graphics)
    goto(maturin2,graphics,300, -180)
    pendown(maturin2,graphics)
    for i in range(30):
        figure(maturin2, graphics,3,70)
        right(maturin2, 65, graphics)
##Frank circulo externo
def func8():
    penup(frank2,graphics)
    goto(frank2,graphics,300, -180)
    pendown(frank2,graphics)    
    for i in range(60):
        figure(frank2, graphics,8,100)
        right(frank2, 91,graphics)
#####################################################          
##MAturin Circulo interno
def func9():
    penup(maturin3,graphics)
    goto(maturin3,graphics,-300, -180)
    pendown(maturin3,graphics)
    for i in range(30):
        figure(maturin3, graphics,3,70)
        right(maturin3, 65, graphics)
##Frank circulo externo
def func10():
    penup(frank3,graphics)
    goto(frank3,graphics,-300, -180)
    pendown(frank3,graphics)    
    for i in range(60):
        figure(frank3, graphics,8,100)
        right(frank3, 91,graphics)               
###Hilos de Ejecución
threading.Thread(target=func1).start()
threading.Thread(target=func2).start()
###
threading.Thread(target=func3).start()
threading.Thread(target=func4).start()
###
threading.Thread(target=func5).start()
threading.Thread(target=func6).start()
###
threading.Thread(target=func7).start()
threading.Thread(target=func8).start()
###
threading.Thread(target=func9).start()
threading.Thread(target=func10).start()

screen = generate_screen("black")

process_queue(graphics, screen)

screen.exitonclick()
