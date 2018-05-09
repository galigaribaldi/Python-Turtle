from turtle import *

def Triangulo():
    for i in range(3):
        lt(120)
        fd(100)

def Master():
    for i in range(6):
        Triangulo()
        lt(360/6)

Master()
