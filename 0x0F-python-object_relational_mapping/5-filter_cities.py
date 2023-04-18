#!/usr/bin/python3
"""
takes the name of state as an argument and lists all cities of that state
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
     db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name=%s\
    ORDER BY cities.id"
    num_rows = cur.execute(sql, (argv[4],))
    rows = cur.fetchall()
    result = []
    i = 0
    for row in rows:
        result.append(rows[i][0])
        i += 1
    joined = ", ".join(result)
    print(joined)
    cur.close()
    db.close()
