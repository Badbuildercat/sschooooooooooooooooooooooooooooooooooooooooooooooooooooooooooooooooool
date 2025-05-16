"""
program fixing steps
1 undestand the problem
2, plan the fix
3 make and test the code
4 use it and analize the respons
5 make it better



code flow chart

    Start
      |
      \/
      [input choice C->F or F->C]
      |
      \/
      [input temp]
      |
      \/
      |if choice is C->F| ->then -> [calcutlate C->F]
      |
      \/
      |if choice is F->C| ->then -> [calcutlate F->C]
      |
      \/
      [show resault]
      |
      \/
    End

probly better to make them here instead of in your code writer
https://www.storyboardthat.com/lv/izveidot/darblapas-pl%C5%ABsmas-diagramma#

psudo code

Start
    input "Do you want convert (C->F) or (F->C)?"
    input choice
    input "Enter the tepurature"

    if choice= "C->F" then
        resault=(tempurature *9/5) + 32
        output "Resault is:",result, "F"
    else if choice="F->C" then
        resault=(temperature - 32)*5/9
        output "Resault is:",result, "C"
    else
        output "Incompatible input"
End
"""

def c_to_f(celsius):
    return (celsius * 9/5) + 32 

def f_to_c(fahrenheit): 
    return (fahrenheit - 32) * 5/9 

try:
    choice=input("Do you want to convert (C->F) or (F->C)?").strip().upper()
    temp=float(input("Input temperature: "))

    if choice == "C->F":
        print(f"The resault is: {c_to_f(temp):.2f}F")
    elif choice == "F->C":
        print(f"The resault is: {f_to_c(temp):.2f}C")
    else:
        print("Incompatible resault")
except ValueError:
    print("Great now you broke it what am i suppost to do with this mess you have made. How Stupid do you have to be to not put somthing that is said infront of you or being even less of a capable person and not put a number when it asks for the temperature do you think it wants the temperature in words? No how stupid can you possibly be to mess up such an imposibly easy task its incomprehensible how stupid you are to even see this message because it would require you fail at a cosmic level")

import tkinter as tk


#looks like we are doing this again

def c_to_f(celsius):
    return (celsius * 9/5) + 32 

def f_to_c(fahrenheit): 
    return (fahrenheit - 32) * 5/9

def convert_temp():
    try:
        temp=float(enter.get())
        if var.get()==1:
          result=c_to_f(temp)
          resault.config("the result is",result)
        elif var.get()==1:
            result=f_to_c(temp)
            resault.config("the result is",result)
        else:
            resault.config("GO KILL YOUR SELF")
    except ValueError:
        print("GO KILL YOUR SELF")




#time to get to the root of this one
root=tk.Tk()
root.title("Man do i love adding pointless titles with random text of me complaining")

var=tk.IntVar()
radiof=tk.Radiobutton(root, text="C to F", variable=var, value=1)
radioc=tk.Radiobutton(root, text="F to C", variable=var, value=2)

input=tk.Label(root, text="Input temperature")
enter=tk.Entry(root)

button=tk.Button(root, text="conversion", command=convert_temp)

resault=tk.Label(root, text="")

#pack those fools
radiof.pack()
radioc.pack()
input.pack()
enter.pack()
button.pack()
resault.pack()


#time to loop that thing
root.mainloop()