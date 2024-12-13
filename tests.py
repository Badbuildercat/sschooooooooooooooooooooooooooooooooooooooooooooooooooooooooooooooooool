import sqlite3

conn=sqlite3.connect(database='test.db')


c=conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS tornis(
          maaja TEXT,
          kods TEXT
)''')

data=[
    ('Lauku iela 12', '698723'),
    ('Rīgas iela 30', '420561'),
    ('Zaķu iela 13', '169420')
]


c.executemany('INSERT INTO tornis(maaja,kods) VALUES (?,?)',data)


conn.commit()
conn.close()