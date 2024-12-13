"""text files 
open()
which files we opening
text files - .txt .csv .... JSON
open has 4 modes 
r - read, open the file to read
a - add, open the file to add stuff to it and make a new one if doesnt exist
w - write, open file to write stuf make a new one if doest exist
x - make, makes a new file with the name
readline() read certin lines
write/and make files
when deleting you need to make sure the file already
exists before it can be deleted
"""
def read_data():
    data_name=input("endter file name: ")#ask to enter files name
    try:
        with open(data_name, 'r', encoding='utf8') as files:
            contents=files.read()
            print(contents)
    except FileExistsError:
        print("smothin aint right here")
    except FileNotFoundError:
        print("either this dont exist or you cant spell") 

if __name__=="__main__":
    read_data()

file=open("text file.txt", 'r', encoding='utf8')
for ii in file:
    print(ii)
file.close()

files=open('texts be textin.txt', 'a', encoding='utf8')
files.write("we got som textt to put in the file that ")
files.write("will be riten today and is just more ")
files.write("placeholder text for a differnet file")
files.close()

#open and read
ff=open('texts be textin.txt', 'r', encoding='utf8')
print(ff.read())

#make new files
"""
gg=open('winter.txt', 'x')
kk=open('sumer.txt', 'w')
"""
a=input("write an essay")
print("that input was just there to make you wait")
#deletion
import os
if os.path.exists('winter.txt'):
    os.remove('winter.txt')   
    print("winter has let the chat")
else:
    print("its already gone")    

#file that take you r name
name=input("name now:") 
files=open('text with name', 'a', encoding='utf8') 
files.write(name)

"""
make a file tbelow.txt, which is text
read the text and print it in terminal
get the simbol amaunt and write the first 10
print the first and last simbol
"""

with open('tbelow.txt', 'r', encoding='utf8') as data:
    text=data.read() 
print(text)
#simbol amount in text
amount=len(text)
print(f"simbol amount is {amount}")
#print first 10 smbols
print(f"the first 10 simbols are: {text[:10]}") 
#print first and last simbol
print(f"first and last simbol is {text[0]} {text[len(text)-1]}")





