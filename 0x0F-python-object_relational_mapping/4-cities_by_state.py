#!/usr/bin/python3

"""script that lists all states with a name starting with N from the databse hbtn_0e_0_usa."""

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()
cursor.execute("SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
query_row = cursor.fetchall()
for row in query_row:
    print (row)
cursor.close()
db.close()
