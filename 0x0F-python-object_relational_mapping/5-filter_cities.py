#!/usr/bin/python3

"""script that lists all cities from argument state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = ("""SELECT cities.name FROM states INNER JOIN
                cities ON states.id = cities.state_id WHERE
                states.name LIKE %s ORDER BY cities.id ASC""")
    cursor.execute(query, (argv[4],))
    query_row = cursor.fetchall()
    if (not query_row):
        print('\n')
    i = 0
    for row in query_row:
        i += 1
        stjoin = ''.join(row)
        splitrow = stjoin.split(
            '\'')[len(stjoin.split('\'')) - 1].split('\'')[0]
        if (i == len(query_row)):
            print(splitrow, end='\n')
        else:
            print(splitrow + ', ', end='')
    cursor.close()
    db.close()
