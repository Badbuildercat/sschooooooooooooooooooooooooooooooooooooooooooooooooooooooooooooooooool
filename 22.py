"""
Data base and pysismple

Doesnt work!
"""
import PySimpleGUI as sg
import sqlite3

conn=sqlite3.connect(database='The Joe Rogan show.db')
cursor=conn.cursor()

#make a table if there isnt already one
cursor.execute('''CREATE TABLE IF NOT EXISTS data_to_be_stored_in_a_table(
               id INTEGER PRIMARY KEY, 
               name TEXT, 
               lastname TEXT,
               email TEXT
)''')




conn.commit()

def steal_their_data():
    cursor.execute("SELECT * FROM data_to_be_stored_in_a_table")
    return cursor.fetchall()
def add_user(name, lastname, email):
    cursor.execute("INSERT INTO data_to_be_stored_in_a_table (name, lastname, email VALUE (?,?,?))", (name, lastname, email))
    conn.commit()

parts=[
    [sg.Text('Name'), sg.InputText(key='name')],
    [sg.Text('Lastname'), sg.InputText(key='lastname')],
    [sg.Text('Email'), sg.InputText(key='email')],
    [sg.Button('add'), sg.Button('delete'), sg.Button('Leave')],
    [sg.Table(values=steal_their_data(),headings=['ID', 'Name', 'Last Name', 'email'],key='table', enable_events=True, bind_return_key=True)]
]

window=sg.Window('The saver of data',parts,resizable=True)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='Leave':
        sg.popup_annoying('wow what a suprise it doesnt work now go be a normal person and use the x button')
    if event=='add':
        #yoink the data
        name=value['name']
        lastname=value['lastname']
        email=value['email']
#        if name and lastname and email:
#            add_user(name, lastname, email)
#            window.Element('table').Update(value=steal_their_data())
#            window['name'].update('')
#            window['lastname'].update('')
#            window['email'].update('')
        #save thy data in the data base
       #cursor.execute("INSERT INTO data_to_be_stored_in_a_table (name,lastname,email) VALUES (?,?,?)", (name,lastname,email))
       #conn.commit()
conn.close()