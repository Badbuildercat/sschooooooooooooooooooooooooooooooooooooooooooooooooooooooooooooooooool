import turtle
import random
#make an oject that lets you draw
t=turtle.Turtle()

#sqaure
t.speed(9000)

def change_color():
    colors=["orange","green","#00E9FA","#7E00FA","#E20101","blue","#09E605","#4505E6","#F0E844"]
    t.color(random.choice(colors))


for _ in range(91):
    t.forward(100)
    t.right(91)
    change_color()

t.penup()
t.forward(300)
t.pendown()

for _ in range(36):
    for _ in range(4):
        t.forward(100)
        t.left(90)
    change_color()
    t.right(10)

t.penup()
t.right(90)
t.color("lime")
t.forward(250)
t.pendown()


t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.right(120)
t.end_fill()

t.penup()
t.right(90)
t.forward(250)
t.pendown()

change_color()
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.forward(250)
t.pendown()

for _ in range(4):
    for _ in range(100):
        change_color()
        t.forward(1)
    t.right(90)

t.penup()
t.right(90)
t.forward(100)
t.right(90)
t.forward(10)
t.right(180)
t.pendown()


for _ in range(3):
    for _ in range(120):
        change_color()
        t.forward(1)
    t.right(120)

t.penup()
t.forward(30)
t.left(90)
t.forward(100)
t.right(90)
t.pendown()

for _ in range(4):
    for _ in range(60):
        change_color()
        t.forward(1)
    t.right(90)



turtle.done()