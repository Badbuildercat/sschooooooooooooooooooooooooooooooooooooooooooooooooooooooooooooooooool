"""
intager - numbers
text - text
blob - binary data
real - whatever it is it probly aint real
numerits - line precisioin
________________________
nn - not null cant be 0
pk- primary key checks other lines
ai - auto increment
u - unique
"""

import sqlite3

#get that data over here 
conn=sqlite3.connect(database='The Joe Rogan show.db')

#cursor
c=conn.cursor()

#table
c.execute('''CREATE TABLE IF NOT EXISTS The_Roundest_Table(
          id INTEGER PRIMARY KEY,
          tables TEXT,
          people TEXT
)''')

#data
data=[
    (1, 'the round one', '5'),
    (2, 'its a bit rounder', '7'),
    (3, 'why is this table so round', '8')
]

#data insersion
c.executemany('INSERT INTO The_Roundest_Table(id,tables,people) VALUES (?,?,?)',data)

conn.commit()
conn.close()