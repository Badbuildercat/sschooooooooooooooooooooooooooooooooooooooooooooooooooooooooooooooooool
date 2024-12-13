import matplotlib.pyplot as pit
import numpy as np


name="text wit that textyness.txt"
kat=[]
val1=[]
val2=[]
val3=[]
avr=[]

with open(name, 'r', encoding='utf-8')as t:
    for line in t:
        parts=line.strip().split(',')
        if len(parts)==4:
            katt=parts[0].strip()
            vall1=int(parts[1].strip())
            vall2=int(parts[2].strip())
            vall3=int(parts[3].strip())
            kat.append(katt)
            val1.append(vall1)
            val2.append(vall2)
            val3.append(vall3)

            #find the average number and add it
            vid=(vall1+vall2+vall3)/3
            avr.append(vid)



x=np.arange(len(kat))
width=0.2   # width colum
pit.figure(figsize=(18,8))
pit.bar(x-width, val1,width,label="Invesment", color='#B9FF15') #make the diagram
pit.bar(x,val2,width, label="Profit", color="#4715FF")
pit.bar(x+width,val3,width, label="Sales", color="#FF8215")
pit.plot(x,avr, color="#EC0101", label="average number", linewidth=2)
pit.xlabel("random stuff that was writen")
pit.ylabel("a number with almost no mean but is there anyway")
pit.title("a diagram with more data than it probly needs but who realy cares")
pit.legend()
pit.xticks(x, kat)

pit.show()