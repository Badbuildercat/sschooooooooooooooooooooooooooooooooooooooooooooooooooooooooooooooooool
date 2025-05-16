"""
oh Great another test just what i wanted to do right now
Rules of Engagement are only the answer and 1 word

1. dpl  -| DBVS
2.Tabula  +
3. record  +
4.   -  |  6
5.KEy   -  | CREATE
6. U     - | NN
7. integer  - | REAL
8. main key   -  | AI
9.TEXT +
10 Tabula   - | fails

3/10
"""


#make a table with python even though it is infinitly 
#easier if you just do it through db browser
import sqlite3

def make_database():
    connection=sqlite3.connect("The Joe Rogan Show.db")
    worker=connection.cursor()

    worker.execute("""
CREATE TABLE IF NOT EXISTS another_interesting_table_that_needs_to_be_made_in_python(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   lastname TEXT, 
                   city TEXT,
                   age INTEGER
                   )
""")
    connection.commit()
    connection.close()



def input_data():
    connection=sqlite3.connect("The Joe Rogan Show.db")
    worker=connection.cursor()
    with open("TExt again how much text can there possibly be.txt", "r", encoding="utf-8") as stuff:
        for line in stuff:
            part=line.strip().split(", ")
            name, lastname, city, age =part
            worker.execute("INSERT INTO another_interesting_table_that_needs_to_be_made_in_python(name, lastname, city, age) VALUES(?,?,?,?)",
                                   (name.strip(), lastname.strip(), city.strip(), int(age)))
            connection.commit()
            connection.close()

if __name__=="__main__":
    make_database()
    input_data()




