#operatori
"""
aritmētiskie operatori: +, -, /, *, //, %, **
piešķiršanas operatori: +, +=, -=, *=, /=
salīdinašanas operatori: ==, !=, >, <, <=, >=
loģiskie operatori: and, or, not
identitiātes operatori
dalības operatori
bitu operatori
"""
#aritmētiskie operatori
print(10+10)
print(10//3) #divide with rounding down
print(10%3) #whats left after dividing
print(10**2) #10 sqaured second number determines this

#piešķiršanas operatori
ball=5
print(ball)

ball1=6
ball1+=2 # adds to the previouse one only works with numbers
print(ball1)

ball2=4
ball2-=2
print(ball2)

ball3=10
ball3*=3
print(ball3)

ball4=18
ball4/=9
print(ball4)

#salsalīdinašanas operatori

print(10==3) #shows there they are both the same
print(5==5)# true if they are the same false if not

print(10!=10)#show they are not the same
print(4!=5)#true if they are not the same false if are

#loģiskie operatori
log=5
print(log<5 and log<10) #and means both need to be true
print(log>4 or log==4) # or means one needs to be true
# print not(log<5 and log<4) # not means it will output the oposite answer

#varbut identitiātes operatori ?
print((6+3)*(7+3))



#data types str, int, flout
#random numbers - random() in a library
import random
print(random.randrange(1,1000)) # random nuber from 1 to 1000


print("start of random numbers")#prints random number until one is larger than 950
number=1
amount=0 #counts how many times it ran the code to tell you how many tries it took
while number<950:
    number=random.randrange(1,1000)
    amount+=1
    print(number)
print("end of random numbers final number was:",number, "and it took",amount,"tries")

#simbol strings

a="houses"

print(a[2:5])
print(a[2:])
print(a[-2:])

#zarošanās konstrukcijas
#if, elif, else
# 1. simple if branching
x=10
if x>5:
    print("x is bigger than 5")
    print(x, "is bigger than 10")
    print(f"{x} is a number")# or format it
#2. if-else
y=3
if y%2==0:
    print(y,"is divisable by 2")
else:
    print(y,"is not divisable by 2")

y=30
if y%2==0:
    print(y,"is divisable by 2")
else:
    print(y,"is not divisable by 2")

#3. if-elif-else
z=0
if z>0:
    print(z,"is positive")
elif z<0:
    print(z,"is negitive")
else:
    print(z,"is 0")

z=87
if z>0:
    print(z,"is positive")
elif z<0:
    print(z,"is negitive")
else:
    print(z,"is 0")

z=-123
if z>0:
    print(z,"is positive")
elif z<0:
    print(z,"is negitive")
else:
    print(z,"is 0")

#4. inclusive branching
a=4
b=8
if a>0:
    if b>0:
        print("both are possitive")
    else:
        print("a is possitive b is not")
else:
    print("a is negative")

#5. branching with logicical operator
age=input=20
vote=True
if age>=18 and vote:
    print("you be able to do the thing where he votes")
else:
    print("you can no vote")