#!/usr/bin/python3

"""script that lists all states with a name starting with N from the databse hbtn_0e_0_usa."""

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()
query = ("SELECT * FROM states WHERE name=%s ORDER BY id ASC")
cursor.execute(query, (argv[4],))
query_row = cursor.fetchall()
for row in query_row:
    print (row)
cursor.close()
db.close()
