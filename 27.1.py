"""how to work with data"""

#Part 1 the important tuff


#part 2 the code
data_name=input("enter the datas name, or else... ")

try:
    with open(data_name, "r", encoding='utf-8') as stuff:
        data=stuff.read()
    simbols=len(data)
    print(data)
    print("")
    print("the amount of charecters in this file are",simbols)#if you want to not have spaces counted use strip()
    print("")
    if simbols>0:
        print("first ten characters are:",data[:10])
        print("")
    else:
        print("The TEXT is EMPTY you should kys now")
        print("")
    if simbols>0:
        print("the first character is:",data[0],"the last one is",data[-1])
        print("")
    else:
        print("The TEXT is EMPTY why would you ever give me this file")
        print("")
    length=input("enter a number that will be compared to the length of this fine text you have entered that is if you actualy decided to be a normal person and add a file with text in it and not a nonexistant file or one without text: ")
    if simbols>0 and length.isdigit():
        length=int(length)
        if length>simbols and 10>length:
            print("the number you entered is higher than the amount of words in the pathetic text you entered")
        elif length>simbols:
            print("The text is shorter than the number you entered")
        elif length==simbols:
            print("the lenth and number are the same")
        elif length<simbols:
            print("the number is smaller than the lenght of your text")
        else:
            print("what did you manage to do that the text isnt longer shorter or the same length")
    else:
        print("What did i tell you about adding a file with no text or were you so stupid and could not put a number into the input that specificly asked for a number")   
except FileNotFoundError:
    print("Your data was not found now suffer the consiqences for your actions")

