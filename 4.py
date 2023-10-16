"""
looping konstructions
cycle with number - when you need to do somthin
certin amount of times                                                                                                                    
"""

#for cycle
#for iterating through lists

list=[1,2,3,4,5]
for element in list:
    print(element)

#cycle for when doing list inerval rang.

a=int(input("input number: "))
s=0
for i in range(1, a+1):
    s+=i
print(s)


leters=["aka", "paka", "laka"]
for i in leters:
    print("hello there, " + i + "!")

#oh no not the while cycle

s=0
a=int(input("i need the number:"))
while a>0:
    s+=a
    a=int(input("next "))
print(s)


#while till you get what you want 
number=1
while number<=5:
    number+=1
    print(number)
    '''
    remove number=+1 i dare you
    '''

#break the while ccycle

list=[1,2,3,4,5]
for element in list:
    if element==3:
        continue #start the next iteration
    if element==5:
        break #stops if 5
    print(element)

#enumerate cycle

list=['a', 'b', 'c']
for index, value in enumerate(list):
    print(f"index ir: {index}, value: {value}")

#get them poztive numberss printed from 10 to 10 counting the enpoints

#first option
for number in range(10, 101):
    if number % 2==0:
        print(number)

#second option
for number in range(10,101,2):
    print(number)


#for cycle with list stuff
list=[10,20,30,40,50]
resault=[] # empty list
for number in list:
    resault.append(number*2)
print(resault)

#fr cylce that does list junk
#while cycle that does stuff

input1=''
while input1 !="leave":
    input1=input("enter 'leave', to stop")


#zip function
words=["bob", "dave", "josh"]
age=[20,30,35]
for words, age in zip(words, age):
    print(f"{words} is {age} years oldguy/oldwoman")

