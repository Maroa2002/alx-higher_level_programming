#!/usr/bin/python3
"""
select a state matching state name searched
SQL query safe from SQL injections (using parameterized queries)
parameters: username, password, database, state name searched
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name = %s ORDER BY id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
