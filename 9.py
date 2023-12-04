"""
dictionary
is a data structure element
for saving data values- come in pairs

is made of keys and pairs each key uniqe
dictionarys are sorted and changeable and cant hav duplicates

"""
winter={
        "mark":"ford",
        "elektric":False,
        "modoual":"Mustang",
        "year":1939,
        "color":["red","white","green","blue","orange","black"]
}
#length
print(len(winter))
#how to know what type
print(type(winter))

sumer=dict(name="dave", age="23", country="france")
print(sumer)

import json
#enter file name that you want to use
file_name=input("give me the files name now!!! ")
# opem and read the json file
try:
    with open(file_name, "r", encoding="utf8")as file:
        data=json.load(file)
except FileNotFoundError:
    print("i dont think it exists toady")
except json.JSONDecodeError:
    print("you dont write in json so it aint gonna work")
#turn this thing into a dictionary

winta=dict(data)
#give me the legth
print(f"its the length of {len(winta)} abnormaly large oil tankers")
#i want the keys 
for key in winta.keys():
    print(key)

#give me all the data
for data in winta.values():
    print(data)

#ente key is one check it is another

input_key=input("input the key to find its value:")
if input_key in winta:
    print(f"{input_key}: {winta[input_key]}")
else:
    print(f"{input_key}-it dont exist ")  



filename=input("secondname")

try:
    with open(filename, "r", encoding="utf8")as file:
        a=json.load(file)
except FileNotFoundError:
    print("i dont think it exists toady")
except json.JSONDecodeError:
    print("you dont write in json so it aint gonna work")  

#turn the json into a dictionary
people=dict()


for person in a:
    person_id=person.get('id')
    person_info={
        "vards": person.get("vards"),
        "uzvards":person.get("uzvards"),
        "vecums":person.get("vecums")
    }
    people[person_id]=person_info

for person_id, person_info in people.items():
    print(f"ID {person_id} name {person_info['vards']}, last name {person_info['uzvards'],}, age {person_info['vecums']}")