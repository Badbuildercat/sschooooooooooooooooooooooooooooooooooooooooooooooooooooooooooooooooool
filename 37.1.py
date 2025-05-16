""""
test thing

1. logrīks
2.
3.root=tk.Tk()
4. cycle
5. tk.Button
6.  text=""
7.tk.Entry
8. get
9. Label
10. pack

7/10
"""

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

conn=sqlite3.connect("The Joe Rogan show.db")
c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS great_we_our_making_another_lovly_table_that_we_realy_need( 
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          text TEXT,
          choice TEXT,
          option TEXT) ''')

conn.commit()

def save():
    text1=text.get("1.0", tk.END).strip()
    list1=listy.get()
    option=op.get()

    if not text1 or not list1 or not option:
        messagebox.showwarning("Youre stupid ass messed up","Fill in every thing before clicking save its doesnt take much of a brain to not mess this up yet somehow you did")
    else:
        c.execute("INSERT INTO great_we_our_making_another_lovly_table_that_we_realy_need(text, choice, option) VALUES (?,?,?)",(text1,list1,option))
        conn.commit()
        messagebox.showinfo("saved","You managed to save somthing")
        messagebox.showerror("delete thing","so it was suposed to delete every thing you inputed and let you write more but that doesnt work so now you have this long message that is just telling you that you have to delete the text if you want to put somthing else in the input and then add that to the table")


root=tk.Tk()
root.title("Why do we make so many of these and why do they all need to be named youd think im running out of stuff to write here but if i wanted to i could make this a lot longer than it already is but i dont realy feel like typing that much and i have to actauly write code and not and obserdly long title for this window")

tk.Label(root, text="input your life story because we have as much room as you need").pack()
text=tk.Text(root, height=5, width=50)
text.pack()
tk.Label(root, text="choose your destiny").pack()
listy=ttk.Combobox(root, values=["     ","running","falling","balling","crawling","mauling","stalling"] )
listy.pack()

tk.Label(root, text="pick an option that has almost no real effect on anything you actualy do").pack()
op=tk.StringVar(value="1")
tk.Radiobutton(root, text="I will do what ever this thing wants me to do", variable=op, value="I will do what ever this thing wants me to do").pack()
tk.Radiobutton(root, text="I will not do what ever this thing wants me to do", variable=op, value="I will not do what ever this thing wants me to do").pack()

tk.Button(root, text="save this random mess you made", bg="#89A203", command=save).pack()















root.mainloop()