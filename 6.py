#version control tools
#repository where you shove yor stuff
#print all even numbers betweaan 130 - 150

for number in range(130, 151):
    if number % 2==0:
        print(number) #who doesnt love useing old code

#print all numbers from 5 to 89 that divides wih 5 3 2

for number in range(15, 89):
    if number % 5==0:
        if number % 3==0:
            if number % 2==0:
                print(number)  #dont look at this is
                #works but should look diferent

for number in range(15, 89):
    if number % 5==0 and number % 3==0 and number % 2==0:
        print(number) #should look like this
