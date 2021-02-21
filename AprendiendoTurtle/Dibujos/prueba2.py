#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import *
from time import *
speed(13)
def circulos():
	for i in range(50):
		circle(5*i)
		circle(-5*i)
		left(i)

def figura(tamano, lados, giros):
	for i in range(lados):
		forward(tamano)
		left(int(giros))

circulos()
def Ran():
	for i in range(30):
		figura(3*i, 3, (360/3))
		left(i)
	exitonclick()
