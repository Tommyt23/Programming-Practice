# Using tutorial: https://www.futurelearn.com/courses/object-oriented-principles/21/todo
from turtle import Turtle
from random import randint

a = Turtle()
b = Turtle()
c = Turtle()
d = Turtle()

a.color('red')
a.shape('turtle')
a.penup()
a.goto(-160, 100)
a.pendown()

b.color('blue')
b.shape('turtle')
b.penup()
b.goto(-160, 70)
b.pendown()

c.color('green')
c.shape('turtle')
c.penup()
c.goto(-160, 40)
c.pendown()

d.color('yellow')
d.shape('turtle')
d.penup()
d.goto(-160, 10)
d.pendown()

for movement in range(100):
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))