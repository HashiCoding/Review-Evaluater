import sqlite3



def train(Review,eval):
    conn = sqlite3.connect('review.db')
    cur = conn.cursor()

    if eval=="POSITIVE":
        Overall = 5
    else:
        Overall = 1


    list =[]
    tuple = (str(10001),str(Review),str(Overall))
    list.append(tuple)

    #print(list)

    # insert data into a table
    cur.executemany("INSERT INTO reviews VALUES(?,?,?)",list)
    conn.commit()

    # commit changes
    conn.commit()

    # close the connection
    conn.close()




