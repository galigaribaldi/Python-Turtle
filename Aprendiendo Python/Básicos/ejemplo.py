from turtle import *

def figura():
	color("red", "yellow")
	title("ventana")
	begin_fill()
	while True:
		forward(200)
		left(170)
		if abs(pos()) < 1:
			break
	end_fill()
	done()
figura( )