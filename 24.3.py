import turtle
import random

t=turtle.Turtle()

def change_color():
    colors=["orange","green","#00E9FA","#7E00FA","#E20101","blue","#09E605","#4505E6","#F0E844"]
    t.color(random.choice(colors))


def branches(br, angle):
    if br>5:
        change_color()
        t.forward(br)
        t.right(angle)
        branches(br-15, angle)
        t.left(2*angle)
        branches(br-15, angle)
        t.right(angle)
        t.backward(br)
    

def tree(tr, angle):
    t.left(90)
    t.penup()
    t.backward(tr)
    t.pendown()
    change_color()
    t.forward(tr)
    change_color()
    branches(tr, angle)


t.speed(0)
t.penup()
t.goto(-200,-200)
t.pendown()
tree(300,30)


turtle.done()