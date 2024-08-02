from turtle import Turtle, Screen
from random import choice

tim = Turtle()
screen = Screen()

colors = ['blue', 'medium turquoise', 'lime green', 'gold', 'crimson', 'medium violet red', 'medium purple']

def draw_shape(num_sides):
  for _ in range(num_sides):
    angle = 360 / num_sides
    tim.forward(100)
    tim.left(angle)

for num_sides in range(3, 11):
  tim.color(choice(colors))
  draw_shape(num_sides)
  
  

screen.exitonclick()