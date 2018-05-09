from turtle import *

def Cuadrado():
    for i in range(4):
        fd(100)
        lt(90)

def Master():
    for i in range(2):
        for i in range(4):
            Cuadrado()
            fd(100)
        pu()
        home()
        pd()
        rt(90)
        fd(100)
        lt(90)

Master()
        
