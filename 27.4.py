import matplotlib.pyplot as pit
import numpy as np # didnt need it but easier to copy all
import pandas as pd


# catagories and values

cat=['A', 'B', 'C', 'D', 'E']
val=[23, 17, 35, 29, 12]

pit.bar(cat,val, color="orange")
pit.xlabel("That is catagoricly incoret")
pit.ylabel("we like number and they are here in force")
pit.title("Simply Painful")
pit.show()

