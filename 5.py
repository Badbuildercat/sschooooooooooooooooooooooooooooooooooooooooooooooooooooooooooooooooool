print("hello there")

a="leters that need lettering"

for x in a: #every letter printed one after the other
    print(x)

print(len(a)) #print the length

print("kwaiter" in a) # find this in that
print(a[2:5]) #reed 2 to 5
print(a[:5]) #read start to 5
print(a[-5:-2]) #die

#put in name
name=input("i want your name: ")
if name=="die":
    print("no you")
else:
    print("you are name is:",name)

backwords_name=""#empety name

for leters in name [::-1]:
    backwords_name=backwords_name+leters
print("backwords_name is: "+backwords_name)
"""
leter positions
     field
-3-2-101234
"""

for number in range(1,101):
    if number%3==0 and number%5==0:
         print("fizbuzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
    else:
        print(number)

text=input("text:")
letteramount=0
words=0
print(len(text))

for letters in text:
    if letters.isalpha():
        letteramount+=1
words=text.split(" ")
words+=1

print(f"number of letters is {letteramount}")
print(f"number of words is {words}")

