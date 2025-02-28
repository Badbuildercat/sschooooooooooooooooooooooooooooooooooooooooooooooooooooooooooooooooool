"""
1 input username
2 input password
3 encrypt password
4 save the username and password in the database
5 simulate registering



Functionality
input username and password

encrypt with hashlib.sha256

 ______________________________________________________
|function            | explenation                     |
|____________________|_________________________________|
|password.encode()   | converts text to bytes          |
|hasslib.sha256(...) | make a SHA-256 hash object      |
|.hexdigest()        | retur hash as hexadecimal string|
|____________________|_________________________________|


authentification - answers the question who are you

authorization -what you can do


"""

import sqlite3
import hashlib


conn=sqlite3.connect("The Joe Rogan show.db")

cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE NOT NULL,
               password_hash TEXT NOT NULL) ''')

conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username=input("Username: ")
    password=input("Password: ")
    password_hash=hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?,?)",(username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        print("why are you so unstable get a grip on yourself ")

def login_user():
    username=input("Username: ")
    password=input("Password: ")
    password_hash=hash_password(password)

    cursor.execute("SELECT * FROM users WHERE username-? AND password_hash=?",(username, password_hash))
    user=cursor.fetchone()
    if user:
        print("Congrats you didnt mess up your password or username")
    else:
        print("Imagine not even being able to remember your username or password")






while True:
    print("\n 1. register \n 2. login \n 3. logout")
    choice=input("choose an action")
    if choice=="1":
        register_user()
    elif choice=="2":
        login_user()
    elif choice=="3":
        break
    else:
        print("look which pipe brain couldnt even enter the number 1 2 or 3 into the input like seriosly how dumb are you its 3 nubers and you failed to write one of them")