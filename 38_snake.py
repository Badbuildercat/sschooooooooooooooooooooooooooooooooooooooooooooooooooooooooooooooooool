import tkinter as tk
from tkinter import ttk, messagebox
import random
from PIL import Image, ImageTk

def not_happening():
        popupBonusWindow = tk.Tk()
        popupBonusWindow.wm_title("Your worst nightmare")
        labelBonus = tk.Label(popupBonusWindow, text="i do not care what window maker you are useing but i will never make the exit button work just be normal and use the x button")
        labelBonus.pack()
        b1=tk.Button(popupBonusWindow, text="Exit", command=lambda: [not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening()])
        b1.pack()

WIDTH, HEIGHT = 1000, 1000
CELL = 50
MOVE = {
    "Up": (0, -CELL),
    "Down": (0, CELL),
    "Left": (-CELL, 0),
    "Right": (CELL, 0)
}



root = tk.Tk()
root.title("Snake Game")
root.iconbitmap("Goofy individual.ico")

menu_bar=tk.Menu(root)
file_menu=tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Close", command=not_happening)
menu_bar.add_cascade(label="File", menu=file_menu)


root.config(menu=menu_bar)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = [(CELL * 3, CELL * 3), (CELL * 2, CELL * 3), (CELL, CELL * 3)]
direction = "Right"
redstuff = (CELL * 5, CELL * 5)
running = True


food_image = Image.open("food_image.png")  
food_image = food_image.resize((CELL, CELL))  
food_photo = ImageTk.PhotoImage(food_image)

snake_image = Image.open("snake_image.png")  
snake_image = snake_image.resize((CELL, CELL))  
snake_photo = ImageTk.PhotoImage(snake_image)
score=0
def update():
    global snake, redstuff, running, score
    if not running:
        return
    
    x, y = snake[0]
    dx, dy = MOVE[direction]
    new_head = (x + dx, y + dy)

    if (new_head in snake) or (not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT)):
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"You are now dead. Please get better at the game if you don't want to see this text as often.", fill="red",font=("Times new roman", 20))
        canvas.create_text(WIDTH // 2, (HEIGHT // 2)+30, text=f"Your score was {score}", fill="red",font=("Times new roman", 20))
        running = False
        return
    
    snake.insert(0, new_head)

    if new_head == redstuff:
        score+=1
        redstuff = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
    else:
        snake.pop()
    
    draw()
    root.after(250, update)

def change_direction(event):
    global direction
    if (event.keysym=="Up" and direction!="Down") or \
       (event.keysym=="Down" and direction!="Up") or \
       (event.keysym=="Left" and direction!="Right") or \
       (event.keysym=="Right" and direction!="Left"):
        direction=event.keysym

def draw():
    canvas.delete("all")
    x, y = redstuff
    canvas.create_image(x + CELL // 2, y + CELL // 2, image=food_photo)

    for x, y in snake:
        canvas.create_image(x + CELL // 2, y + CELL // 2, image=snake_photo)



draw()
root.bind("<KeyPress>",change_direction)
update()

root.mainloop()