import modulo1 as mod
##Generacion de varias tortugas
frank = mod.generate_Tortugas("", "turtle", 1, 10)
maturn = mod.generate_Tortugas("blue", "arrow", 1, 0)
##Colors
colors =['orange', 'red', 'pink', 'yellow', 'blue', 'green']
##Pantalla
screen = mod.generate_screen("black")
###Acciones 1
#for i in range(30):
#    mod.figura(100, 4, frank, colors[i%6],"")
#    frank.lt(21)
#    mod.circle(50, frank, "blue","")
###Acciones 2
for i in range(30):
    mod.figura(100, 4, frank, colors[i%6],"")
    frank.lt(21)
    mod.circle(50, maturn, "blue","")
    maturn.lt(21)
screen.exitonclick()