import matplotlib.pyplot as pit


name='text is painful.txt'
kat=[]
val=[]


with open(name, mode='r', encoding='utf-8') as pain:
    for line in pain:
        """
        parts=line.strip().split('-')
        if len(parts)==2:
            kat1=parts[0].strip() #alternitvie way of doing thigs
            kat.append(kat1)
            val1=int(parts[1].strip())
            val.append(val1)
        """
        parts=line.split()
        kat.append(parts[0])
        val.append(int(parts[2]))

pit.figure(figsize=(10,6))
pit.bar(kat,val, color='#B9FF15') #bar - colum, plot - line
pit.xlabel('towns that are around')
pit.ylabel('amount if people blown up by russians')
pit.title('amount of things that be happening in the here')
pit.legend()

pit.show()