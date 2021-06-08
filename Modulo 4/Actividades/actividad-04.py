import queue
import threading
import modulo2 as mod
##Generacion de varias tortugas
frank = mod.generate_Tortugas("black", "turtle", 1, 10)
maturn = mod.generate_Tortugas("blue", "arrow", 1, 0)
##Colors
colors =["blue", "medium blue", "navy", "dark blue", "midnight blue", "royal blue"]
##Pantalla
screen = mod.generate_screen("")
###Queue de Reproduccion
graphics = queue.Queue(1) 
###Acciones 2
def accion1():
    mod.pencolor(frank, graphics,"yellow")
    mod.pensize(frank, graphics,4)
    mod.begin_fill(frank, graphics)
    mod.fillcolor(frank, graphics,"blue")    
    for i in range(30):
        mod.figure(frank, graphics, 4,100)#
        mod.left(frank, 21, graphics)
    mod.end_fill(frank, graphics)                

def accion2():
    for i in range(30):
        mod.circle(maturn,graphics,50)#,"",""
        mod.left(maturn, 21, graphics)
    
###Hilos de Ejecución
threading.Thread(target=accion1).start()
threading.Thread(target=accion2).start()

mod.process_queue(graphics, screen)

screen.exitonclick()
