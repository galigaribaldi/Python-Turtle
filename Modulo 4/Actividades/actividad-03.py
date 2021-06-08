from multiprocessing import Process
import modulo1 as mod
###Generacion de Tortugas
frank = mod.generate_Tortugas("","turtle",1,7)
maturin = mod.generate_Tortugas("","turtle",1,7)
###Generacion de pantallas
screen  = mod.generate_screen("")
###Acciones
##Accion 1
def accion1():
    mod.circle(100, frank,"black","")
##Accion 2
def accion2():
    mod.circle(100, maturin,"black","")

###Importando procesos
if __name__ == '__main__':
    p1 = Process(target=accion1)
    p1.start()
    p2 = Process(target=accion2)
    p2.start()
    p1.join()
    p2.join()
    ##Pantalla
    screen = mod.generate_screen("black")