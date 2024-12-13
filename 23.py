"""
test
1 .conect() +
2 .execute() +
3 .commit()+
4  cursor +
5  -
6 -
7 .close() - 
8 .db +
9 -
10 uniqe -


make some fancy aplication
"""

import PySimpleGUI as sg
import sqlite3
from datetime import datetime

conn=sqlite3.connect(database='The Joe Rogan show.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS their_flying_in(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               lastname TEXT,
               gender TEXT,
               age INTEGER,
               date TEXT
)''')
conn.commit()

parts=[
    [sg.Text('Name'), sg.InputText(key='name')],
    [sg.Text('Lastname'), sg.InputText(key='lastname')],
    [sg.Radio('Male','1', key='gm'), sg.Radio('Female','1', key='gf')],
    [sg.Text('Age'), sg.Combo([i for i in range(1, 100001)],key='age')],
    [sg.Text('Date'), sg.CalendarButton('Chose a date', target='date', key='date')],
    [sg.Button('Register'), sg.Button('Leave')]
]

window=sg.Window('they be flying in',parts,resizable=True)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='Leave':
        sg.popup_annoying('I wonder what compels you to add these buttons they are pointless just use the x button its easier')
    if event=='Register':
        name=value['name']
        lastname=value['lastname']
        gender='Male' if value['gm'] else 'Female'
        age=int(value['age'])
        date=value['date']
        cursor.execute('''INSERT INTO their_flying_in(name, lastname, gender, age, date)
                       VALUES (?,?,?,?,?) ''',(name, lastname, gender, age, date))
        conn.commit()
        sg.popup_annoying('congradulations you actauly managed to register and the system didnt crash')
conn.close()