import matplotlib.pyplot as pit
import numpy as np
import pandas as pd


# catagories and values

cat=[]
val=[]

#read the data from the file because its fun

with open("text data.txt", "r", encoding='utf-8') as f:
    for line in f:
        parts=line.split()
        cat.append(parts[0])
        val.append(int(parts[1]))

pit.bar(cat,val, color="#880707")
pit.xlabel("That is catagoricly incoret in all posible ways")
pit.ylabel("we like numbers and they are here in force")
pit.title("Complicatedly Painful")
pit.show()

