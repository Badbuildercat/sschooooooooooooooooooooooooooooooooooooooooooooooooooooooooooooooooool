import turtle
import random

def change_color():
    colors=["orange","green","#00E9FA","#7E00FA","#E20101","blue","#09E605","#4505E6","#F0E844"]
    t.color(random.choice(colors))


def draw(t,order,size):
    if order==0:
        t.forward(size)
    else:
        for angle in [60,-120,60,0]:
            draw(t, order-1, size/3)
            change_color()
            t.left(angle)


t=turtle.Turtle()
t.speed(1000)
t.penup()
t.goto(-150,90)
t.pendown()

for _ in range(3):
    draw(t, 4, 300)
    t.right(120)

t.penup()
t.goto(-15000,90)
t.pendown()

turtle.done()