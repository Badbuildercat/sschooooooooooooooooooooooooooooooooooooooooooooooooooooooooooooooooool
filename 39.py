import tkinter as tk
import random

root=tk.Tk()
root.title("the game be ponging")
root.iconbitmap("Goofy individual.ico")
canvas=tk.Canvas(root,width=400,height=400,bg="black")
canvas.pack()

widx=150
widy=350
widh=10
widw=100
platfrom=canvas.create_rectangle(widx,widy,widx+widw,widy+widh,fill="#5F0C87")

ballr=10
ball=canvas.create_oval(0,0,ballr*2,ballr*2, fill="#99F91A")
ballx=random.randint(0,400-ballr*2)
canvas.move(ball, ballx,0)

fall=5
direct=0

def left(event):
    global direct
    direct=-1

def right(event):
    global direct
    direct=1

def stay(event):
    global direct
    direct=0

canvas.bind_all("<KeyPress-Left>", left)
canvas.bind_all("<KeyPress-Right>", right)
canvas.bind_all("<KeyRelease-Left>", stay)
canvas.bind_all("<KeyRelease-Right>", stay)

def game():
    global ball, ballx
    bcord=canvas.coords(ball)
    pcord=canvas.coords(platfrom)
    canvas.move(ball,0,fall)

    if bcord[3]>=pcord[1] and bcord[0]<=pcord[0] and bcord[2]<=pcord[2]:
        newball()
    elif bcord[3]>400:
        canvas.create_text(200,200,text="you died get better at this game you looser", fill="red")
        return
    if direct!=0:
        if pcord[0]+direct*10 and pcord[2]+direct*10<=400:
            canvas.move(platfrom, direct*10,0)
    root.after(30, game)

def newball():
    global ball
    canvas.delete(ball)
    x=random.randint(0,400-ballr*2)
    ball=canvas.create_oval(0,0, ballr*2, fill="#99F91A")
    canvas.move(ball,x,0)









game()
root.mainloop()