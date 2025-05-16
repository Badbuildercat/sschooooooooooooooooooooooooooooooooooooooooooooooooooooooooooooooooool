import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

root=tk.Tk()
root.title("once again we have to make a title that is quite long and almost pointless because i dont care enough to make a title that is acurate to what is being made but im willing to type out a overly long title that is just me ranting about something random and unimportant to anyone including myself")
root.iconbitmap("Goofy individual.ico")
root.geometry("1000x500")

backgroundimag=Image.open("Exploding Chair.png")
backgroundimag.resize((1000,500), Image.Resampling.LANCZOS)
backimage=ImageTk.PhotoImage(backgroundimag)
canvas=tk.Canvas(root, width=1000, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0,image=backimage, anchor="nw")

entry=tk.Entry(root, font=("Times new roman", 14))
entry_window=canvas.create_window(500,50, window=entry, width=100)

start_button=tk.Button(root, text="Start the countdown to the end of time",font=("Times new roman", 14), bg="red", fg="orange" )
button_window=canvas.create_window(500,100, window=start_button)

timer=tk.Label(root, text="00:00", font=("Times new roman", 40), fg="orange", bg="red" )
timer_window=canvas.create_window(500,430, window=timer)


root.mainloop()