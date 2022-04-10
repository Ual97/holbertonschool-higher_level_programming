#!/usr/bin/python3

"""script that lists all values in states
 where name matches the argument. """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    qry = """SELECT *
             FROM states
             WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cursor.execute(qry)
    query_row = cursor.fetchall()
    for row in query_row:
        print(row)
    cursor.close()
    db.close()
