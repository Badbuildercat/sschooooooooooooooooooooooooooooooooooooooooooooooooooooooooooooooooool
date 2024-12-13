#cycle constructions - for and while

#my version
a=1
while a<6:
    print(a)
    a+=1

#teachers version
for i in range(1,6):
    print(i)



list=['apple','carrot','chery']

for lists in list:
    print(lists)


# my version
b=2
while b<21:
    print(b)
    b+=2

#my modified version
c=1 
while c<21:
    if c%2==0:
        print(c)
    c+=1

#teachers easy version
for i in range(2,21,2):
    print(i)

#teachers hard version
for i in range(1,21):
    if i%2==0:
        print(i)


#hard way
sqaured=[ i **2 for i in range(1,11)]
print(sqaured)
"""
for i in sqaured:
    print(i)
"""

#easy way yeah right doesnt even work
"""
sqaured2=list(range(1,11))
empty=[]
for i in sqaured2:
    sq=i**2
    empty.append(sq)
print(empty)
"""
import math

def print_fakt(number):
    for i in number:
        print("number",i,"factorial is",math.factorial(i))

print_fakt([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("number 21 factorial is way to much")


# took her long enough to get to while cycles


#i think ive seen this bit of code before
a=1
while a<6:
    print(a)
    a+=1

sum=0
i=1

while i<10:
    sum+=i
    print(i)
    i+=1
print(sum)

i=10
while i>=1:
    print(i)
    i-=1

input_input=""
while input_input.lower()!="exit":
    input_input=input("type exit to exit: ")
    if input_input=="exit":
        print("Exiting program")
    else:
        print("you entered:",input_input)



number=[]

while True:
    try:
        numbers=int(input("Inpuut number:"))
        number.append(numbers)
    except ValueError:
        print("something is very wrong but i have no idea what it is or how to fix it so good luck")
        break