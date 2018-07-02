#!/usr/bin/python3.5
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    # Docker internal ip, will need to expose it when connecting externally
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='172.17.0.2' password='password'")
    print("it works fam \n")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM appIdTable;""")
    rows = cur.fetchall()

    print("\nCurrent Table data:\n")
    for row in rows:
        print(str(row[0]) + " : " + str(row[1]))

except:
    print("ERROR Connecting to database")
