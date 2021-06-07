from multiprocessing import Process
import turtle

t1=turtle.Turtle()
t2=turtle.Turtle()

def tes1():
  t1.speed(0)
  i=0
  while i < 360:
    t1.forward(1)
    t1.left(1)
    i+=1

def tes2():
  t2.speed(0)
  i=0
  while i < 360:
    t2.forward(1)
    t2.right(1)
    i+=1

if __name__ == '__main__':
  p1 = Process(target=tes1)
  p1.start()
  p2 = Process(target=tes2)
  p2.start()
  p1.join()
  p2.join()