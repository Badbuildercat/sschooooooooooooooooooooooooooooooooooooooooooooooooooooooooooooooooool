"""
how are window tools made

header window - file name thing name and an icon and the 
3 magic buttons
tool window - all them tools
information window - information
______________________________
Librarys
tkinter, pysimple

1. import the tkinter model
2. make the main program window
3. add the tools
4. name the main window
_______________________________
geomatry makning
1 pack methode    (pady=10) for padding
2 grid methode
3 place methode "the only good one"
_______________________
window tools
1. text lable
2. text window
3. button
4. pick a sqaure
5. list
6. text box
"""
#import
from tkinter import*
from tkinter import messagebox
#make the window
window=Tk()
#how to change icon
window.iconbitmap('sv.ico')
window.geometry("500x300+100+50")
window.title("have you come to give us your stuff?")
# add buttons
"""

all a waste

red_button=Button(window, text="red", fg="red")
red_button.pack(side=LEFT)
red_button=Button(window, text="green", fg="green")
red_button.pack(side=TOP)
red_button=Button(window, text="blue", fg="blue")
red_button.pack(side=BOTTOM)
red_button=Button(window, text="yellow", fg="yellow")
red_button.pack(side=RIGHT)

now we grid
"""
"""
also useles

red_button=Button(window, text="red", fg="red")
red_button.grid(row=0, column=2)
name1=Label(window, text="name").grid(row=1, column=3)
input1=Entry(window).grid(row=1, column=4)
name2=Label(window, text="last name").grid(row=2, column=3)
input2=Entry(window).grid(row=2, column=4)

time to place

"""
def intresting_mesage():
    name=input1.get()
    messagebox.showinfo("acusation", f"Youre a comunist {name}!")

name1=Label(window, text="name")
name1.place(x=50, y=50)
input1=Entry(window)
input1.place(x=100, y=50)

#make a window where you put your name
#and push a button to get a thing

input_window=Entry(window, width=30)
input_window.place(x=0, y=100)

thing_button=Button(window, text="press me", command=intresting_mesage)
thing_button.place(x=200, y=100)






#start doing
window.mainloop()