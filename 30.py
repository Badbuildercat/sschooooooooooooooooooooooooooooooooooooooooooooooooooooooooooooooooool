"""
LIST

lists start with the index 0 first number is 0
to get a value you need to know its index
the lists length is not the last index
the last indext is = the lists length -1 (list has 10 things in it least index is 9 not 10 or just write -1 for last -2 for second to lst and so on)
to print a specific thing in the list you need to use print(list["index"])
woring with lists is normaly done with cycles


LIBRARY
to get a value from a library you need to know its key
 ____________________________________
|value |dave | 7        |IT          |
|______|_____|__________|____________|
|key   |name |experiance|education   |
|______|_____|__________|____________|

library= {'name':'dave','experiance':7, 'education':'IT'}
to get the name you would use
print(library['name'])

COMBINED LIBRARY LIST
Librarys are often used in combination with lists as values in the list

people =[
    {'name':'dave','experiance':7, 'education':'IT'},
    {'name':'joe','experiance':9, 'education':'IT'}
]

for person in people:
    print(person['name'])

this code prints out the names of every person in the list

TEST PART
Self rating 10/10
Real rating 9/10
"""
import os
import matplotlib.pyplot as pit

def read_file(name):
    if not os.path.exists(name):
        print("You truly are a stupid individual how could you input a file that does not exist or managed to misspell the files name")
        return None
    else:
        with open(name, 'r', encoding='utf-8') as file:
            content=file.readlines()
        return content
    
def analyze_content(content, length):
    all_symbols="".join(content)# add the content to the empty text box
    print("symbol amount in the file:",len(all_symbols),)
    print("the first 10 symbols are:", all_symbols[:10]) #[start:end]
    print("the first symbol is:",all_symbols[0],"and the last symbol is:",all_symbols[-1])
    if length.isdigit():
        length=int(length)
        print("The symbols from the begening to that number you entered are:",all_symbols[:length])
    else:
        print("how the hell did you manage to scew up such an easy task all you had to do was input a number and yet somhow you failed at the simple task a 3 year old could do")
        
def create_chart(content):
    letters=[]
    values=[]
    for line in content:
        parts=line.strip().split()
        if len(parts)==2:
            letters.append(parts[0])
            try:
                values.append(float(parts[1]))
            except ValueError:
                print("You are stupid")
        else:
            print("I dont know if your stupid smart or just lucky because i dont even know how to mess things up to get this error mesage")
    pit.bar(letters, values)
    pit.title("a whole lot of pain and suffering in a hole")
    pit.xlabel("theres to many of them retreat")
    pit.ylabel("they have breached the defences")
    pit.show()

#name=input("Text file needs to be inputed i know its very anoying and i would rather just write it in once and have it always use that but unfortunatly it asked for an input and so i delivered")

if __name__=="__main__":
    name=("text with some wird data.txt")#replace with the commented text later
    content=read_file(name)
    if content is not None:
        length=input("WHy is there another input? what could we not find a way to get a length without asing whoevers using this code")
        analyze_content(content, length)

        create_chart(content)