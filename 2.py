#ka lietotajam ievadīt datus?
big=input("ievadit savu vardu:   ")
print(type(big))

#plusošanas kalkolators
big1=float(input("first number"))
big2=float(input("second number"))
big3=big1*big2
print(big1+big2)
#vieglais
print(big3)
#naidīgais
print(f"rezultāts ir {big3}")

"""
vienads a == b
nevienads a=! b
mazksa par a < b
mazaks vai vienads a <= b
"""
#age
vecums=int(input("age"))
if vecums>=100:
    print("your dead")
elif vecums>=18:
    print("your old")
else:
    print("you no old")  

#weather
notikums=(input("weather"))

if notikums=="sun":
    print("sun do be sunning")
elif notikums=="rain":
    print("we do be getting wet")
elif notikums=="snow":
    print("white stuff be faling from the sky")
elif notikums=="cotton":
    print("the cotton pickers be picking very agressivly today")
else:
    print("sumthin be hapening but i dont know what")

#blue stuff

age=int(input("age?"))
can_drive=(input("can drive?"))
if age>=18:
    if can_drive=="true":
        print("you old and can drive")
    else:
        print("you old but no driving")
else:
    if can_drive=="true":
        print("you aint old but can drive")
    else:
        print("you aint old enough")


#is it posotive negative or 0

number=int(input("add number"))
if number==0:
    print("number is zero")
elif number>0:
    print("number is posotive")
else:
    print("number is negative")

#is number even or odd

evenizer=int(input("is it even or not"))

if evenizer==0:
    print("0")
elif evenizer%2==0:
    print("even")
else:
    print("odd")

#figure out wich is bigger

number1=int(input("first numba"))
number2=int(input("second numba"))
if number1>number2:
    print("number 1 is bigger")
elif number2>number1:
    print("number 2 is bigger")
else:
    print("they are the same")

#is the number divisible by 3

number3=int(input("can it be done with a 3"))

if number3%3==0:
    print("can divide with 3")
else:
    print("not divisible with 3")
    