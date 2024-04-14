# Dakota Wrigley
# 16.8 in 'Things To Do'

import csv
import sqlite3
import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
MetaData = MetaData()

conn = sqlite3.connect('books.db')
conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS books
             (title TEXT, author TEXT, year INTEGER)''')

with open('books2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        conn.execute("INSERT INTO books VALUES (?, ?, ?)", row)
conn.commit()
conn.close()

engine = create_engine('sqlite:///books.db')
MetaData.reflect(bind=engine)
books_table = MetaData.tables['books']

connection = engine.connect()
select_query = books_table.select().order_by(books_table.c.title)
result = connection.execute(select_query)
print("Let's print the title column in alphabetical order!")
for row in result:
    print(row[0])