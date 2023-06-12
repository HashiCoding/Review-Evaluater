import sqlite3
import pandas as pd

# this will connect to the given name , if there is no any database it will create a new database in directory 
conn = sqlite3.connect('review.db')
df = pd.read_csv('reviews.csv')

# create a cursor
cur = conn.cursor()

# create a table

cur.execute(""" CREATE TABLE reviews (       
    No text, 
    Review text,
     text
)""")

for index,row in df.iterrows():
    No = row[0]
    Review = row[1]
    Overall = row[2]

    list = []
    tuple = (str(No),str(Review),str(Overall))
    list.append(tuple)

    print(list)

    # insert data into a table
    cur.executemany("INSERT INTO reviews VALUES(?,?,?)",list)
    conn.commit()

# commit changes
conn.commit()

# close the connection
conn.close()






