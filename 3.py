#dalības operatori
# in , not in
leter="t"
word=(input("word"))

if leter in word:
    print("the leter t be letering in the word")
else:
    print("no t")

#and or

s=3000
t=1000

if s>t and t%2 == 0:
    print("its tru")
else:
    print("nope ")


x=200
y=1000

if((x<y) or (y%11==0)):
    print("somthing works")
else:
    print("nothing works")

#pass

c=100
z=4

if  x<y:
    pass
print("you passed")

#lambda function

l=lambda a: a+10
print(l(5))

ai=lambda t,u: t*u
print(ai(5,6))

ui=lambda a,b,c: a+c+b
print(ui(12,34,8))

h=lambda k: k**5 if k%5==0 else k**7
print(h(2))

#program that checkes 
#if the number divides with 5 and 7

number=int(input("number1"))

if (number%5==0) and (number%7==0):
    print("its is a good number")
else:
    print("wrong numbeer")

#def - keyword
#use to make or define a funtcion

def funcion_name():
    print("placeholder text")

sumer=funcion_name()
print(sumer)

#question 1 - multiple names and functions, lambda

def pick_number(skaitlis):
    action={
        "a": lambda x: x**2,
        "b": lambda x: x**3,
        "c": lambda x: x*2,
}
    if skaitlis>10:
        rezultats=action["a"](skaitlis)
    elif skaitlis<-10:
        rezultats=action["b"](skaitlis)
    else:
        rezultats=action["c"](skaitlis)
    return rezultats
rez=pick_number(11)
print(rez)

#lota stuff

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,2,3,4,5]

filtered_list=list(filter(lambda x: x%2==0, list1))
print("its even then",filtered_list)

#map - each number is done

double_list=list(map(lambda x: x*2, list2))
print("doubled list:",double_list)

#numba 4 many things and functions
#teraro operaor usagage

number=7

rez="pozitive" if number>0 else "its not biger then 0"
print(rez)


x=10
y=20
bigger=x if x>y else y
print(bigger)

#how are we aleady at 5
'''
user puts in 2 numbers make a program that compares the numbers
making a function with parameters 
'''

def compare_number(number1, number2):
    if number1>0 and number2>0:
        return "both are positive"
    elif number1<0 and number2<0:
        return "both are negative"
    elif number1==0 or number2==0:
        return "atleast one is 0"
    else:
        return "its somthing else" 
num1=int(input("number1"))
num2=int(input("number2"))
resault=compare_number(num1, num2)
print(resault)

#not the sixth one - multiple things and funtioncs with a sprinkle of lambda

def validate_name(name):
    if len(name) <3:
        return "name is to short you fool"
    elif len(name)>20:
        return "why so long man" 
    elif not name.isalpha():
        return "how dare you use numbers"
    else:
        return "finaly you got something that works"    
name1=input("insert name")
rezult=validate_name(name1)
print(rezult)
#dont look at this the teacher removed the stuff before i finished





