from ColabTurtle.Turtle import *
import turtle

initializeTurtle(initial_speed=7)
color_list=['red','purple', 'blue','green','orange','yellow']

for value  in range(360):
  pencolor(color_list[value%6])
  width(int(value/100)+1)
  forward(value/1.5)
  left(59)

  def fib(n):
    #global count
    #count += 1
    if n <= 1:
        return n
    f = fib(n-1) + fib(n-2)
    return f
  
  fib(30)

def moveDisks(n, src, helper, dst):
    if n > 0:
        moveDisks(n-1, src, dst, helper)
        print('Move disk #{} from {} to {}'.format(n, src, dst))
        moveDisks(n-1, helper, src, dst)

moveDisks(3, 'verde', 'roja', 'azul')