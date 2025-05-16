import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

def not_happening():
        popupBonusWindow = tk.Tk()
        popupBonusWindow.wm_title("Your worst nightmare")
        labelBonus = tk.Label(popupBonusWindow, text="i do not care what window maker you are useing but i will never make the exit button work just be normal and use the x button")
        labelBonus.pack()
        b1=tk.Button(popupBonusWindow, text="Exit", command=lambda: [not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening(), not_happening()])
        b1.pack()

def show_about():
        messagebox.showinfo("about","this program is a program and is made using code i know this is very helpful")
    

root=tk.Tk()
root.title("we love giving these windows random names that have no real use")
root.iconbitmap("sv.ico")

conn=sqlite3.connect("The Joe Rogan show.db")
c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS another_random_table_that_is_100_percnt_nesesary( 
          id INTEGER PRIMARY KEY,
          name TEXT,
          age INTEGER) ''')

conn.commit()

def add_user():
        name=entry_name.get()
        age=entry_age.get()

        if name and age.isdigit():
            c.execute("INSERT INTO another_random_table_that_is_100_percnt_nesesary (name, age) VALUES (?,?)",(name, int(age)))
            conn.commit()
            messagebox.showinfo("Congrats","Congradulations you are not stupid")
        else:
            messagebox.showerror("Failure","you are stupid and failed to do anything worth while")

def show_users():
    c.execute("SELECT * FROM another_random_table_that_is_100_percnt_nesesary")
    users=c.fetchall()
    if users:
          user_list="\n".join([f"ID:{user[0]}, name:{user[1]}, age:{user[2]}" for user in users])
    else:
          user_list="No one was stupid enough to make an acount"
    text2.config(text=user_list)

def delete_stuff():
      entry_name.delete(0, tk.END)
      entry_age.delete(0, tk.END)
      text2.config(text="users will be displayed here because we can do that around these parts")

menu1=Menu(root)
root.config(menu=menu1)
file=Menu(menu1, tearoff=0)
menu1.add_cascade(label="File", menu=file)
file.add_command(label="Exit", command=not_happening)
help=Menu(menu1, tearoff=0)
menu1.add_cascade(label="Help", menu=help)
help.add_command(label="About", command=show_about)

lable_name=tk.Label(root, text="name for something but i dont know what for")
lable_name.pack()
entry_name=tk.Entry(root,)
entry_name.pack()

lable_age=tk.Label(root, text="more text that is probly not nessesary")
lable_age.pack()
entry_age=tk.Entry(root,)
entry_age.pack()

button1=tk.Button(root, text="oh boi now we have text you can press", command=add_user)
button1.pack()
button2=tk.Button(root, text="this is getting out hand now there is 2 of them", command=show_users)
button2.pack()
button3=tk.Button(root, text="Now we can delete stuff because we dont like you around here", command=delete_stuff)
button3.pack()

text=tk.Label(root, text="")
text.pack()
text2=tk.Label(root, text="users will be displayed here because we can do that around these parts")
text2.pack()



root.mainloop()

conn.close()