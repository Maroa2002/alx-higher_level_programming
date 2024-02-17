#!/usr/bin/python3
"""
listing cities from state name searched
parameters: username, password, database name, state name
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
    cur.execute("SELECT cities.name\
                FROM cities\
                WHERE cities.state_id =\
                (SELECT states.id\
                FROM states\
                WHERE states.name = %s)\
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    cities_str = ", ".join(city_names)
    print(cities_str)
    cur.close()
    db.close()
