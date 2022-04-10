#!/usr/bin/python3

"""script that makes SQL protected query"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name=%s ORDER BY id ASC")
    cursor.execute(query, (argv[4],))
    query_row = cursor.fetchall()
    for row in query_row:
        print(row)
    cursor.close()
    db.close()
