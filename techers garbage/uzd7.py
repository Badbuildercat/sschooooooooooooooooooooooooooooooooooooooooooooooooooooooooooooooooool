"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""

# this is the way
list1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
list2=[]

for last in list1:
    dokta="Dr. "+last
    list2.append(dokta)
print(list2)

#this is not so much the way
list1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
list2=[]

def add_dokta(lastn):
    return "Dr. "+lastn
list2=list(map(add_dokta, list1))
print(list2)
