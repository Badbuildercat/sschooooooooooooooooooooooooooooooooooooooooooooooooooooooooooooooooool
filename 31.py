import matplotlib.pyplot as pit
# relative amount
with open ('text datualdata.txt', 'r', encoding='utf-8') as data:
    stuff=data.read()






library={}

words=stuff.split()

for word in words:
    word=word.lower()
    if word in library:
        library[word]+=1
    else:
        library[word]=1


for word, amount in library.items():
    print(word,':',amount)

with open('text word amount.txt','w', encoding='utf-8')as output:
    for word, amount in library.items():
        output.write(f"{word}:{amount}\n")

with open('text word amount.txt','r', encoding='utf-8')as file:
    lines=file.readlines()
library2={}
for line in lines:
    word, amount=line.strip().split(':')
    library2[word]=int(amount)

words = list(library2.keys())
amount= list(library2.values())


pit.figure(figsize=(10, 6))
pit.bar(word, amount, color='green')
pit.xlabel("words so many words")
pit.ylabel("we have a number or 2 or 3 or more")
pit.xticks(rotation=45)
pit.tight_layout()


pit.show()