import matplotlib.pyplot as pit


#read the data
name="1.txt"


kat=[]

val1=[]
val2=[]
val3=[]

#open the fail and do stuff to it

with open(name,'r',encoding='utf-8') as ff:
    for line in ff:
        data=line.strip().split("%")
        if len(data)==4:
            katt=data[0].strip()
            vall1=int(data[1].strip())
            vall2=int(data[2].strip())
            vall3=int(data[3].strip())
            kat.append(katt)
            val1.append(vall1)
            val2.append(vall2)
            val3.append(vall3)



mid_val1=sum(val1)/len(val1)
mid_val2=sum(val2)/len(val2)
mid_val3=sum(val3)/len(val3)




x=range(len(kat))
width=0.25

pit.figure(figsize=(10,6))
pit.bar([i-width for i in x],val1,width=width, color="#FFB405", label="hell on earth")
pit.bar(x,val2,width=width, color="#FF05FB", label="methematics")
pit.bar([i+width for i in x],val3,width=width, color="#05C5FF", label="oh god not the train")
#diagram


pit.plot([i-width for i in x],[mid_val1]*len(x), color="lime",linestyle="--", label="lime line")
pit.plot(x,[mid_val2]*len(x), color="green",linestyle="--", label="green line")
pit.plot([i+width for i in x],[mid_val3]*len(x), color="darkgreen",linestyle="--", label="darkgreen line")


pit.xlabel("names so many names")
pit.ylabel("stuff that is full")
pit.title("numbers and words we all love them")
pit.xticks()
pit.legend()

pit.show()

