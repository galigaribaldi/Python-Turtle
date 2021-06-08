###
from random import *
import queue
import threading
from turtle import pendown, penup
###
from modulo2 import * 
##Pantalla
screen = generate_screen("")
##Tortugas Competidoras
frank = generate_Tortugas("black","turtle",1,0)
maturin = generate_Tortugas("blue","circle",1,0)
rafael = generate_Tortugas("green","arrow",1,0)
donatello = generate_Tortugas("blue","arrow",1,0)
###Tortuga trazadora
traza = generate_Tortugas("black","circle",1,0)
##
graphics = queue.Queue(5)  # size = number of hardware threads you have - 1

def trazadora():
    penup(traza, graphics)
    goto(traza, graphics, -140,140)
    for i in range(17):
        write(traza, graphics, str(i))
        right(traza, 90,graphics)
        forward(traza, 10, graphics)
        pendown(traza, graphics)
        forward(traza, 150, graphics)
        penup(traza, graphics)
        backward(traza, graphics,160)
        left(traza, 90, graphics)
        forward(traza,20, graphics)

def competidor(tortuga, graphics,posx, posy):
    penup(tortuga, graphics)
    goto(tortuga, graphics, posx,posy)
    pendown(tortuga, graphics)
    for i in range(100):
        forward(tortuga, randint(1,5), graphics)
    
###Hilos de Ejecución
threading.Thread(target=trazadora).start()
threading.Thread(target=competidor, args=(frank, graphics,-160, 100)).start()
threading.Thread(target=competidor, args=(maturin, graphics,-160, 80)).start()
threading.Thread(target=competidor, args=(rafael, graphics,-160, 60)).start()
threading.Thread(target=competidor, args=(donatello, graphics,-160, 40)).start()
process_queue(graphics, screen)

screen.exitonclick()