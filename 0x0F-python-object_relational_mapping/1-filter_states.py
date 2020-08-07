#!/usr/bin/python3
"""
write a script that list all states with a name starting with N
"""

if __name__ == "__main__":
	import MySQLdb
	from sys import argv
	
	db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
	cur = db.cursor()
	cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
	query_rows = cur.fetchall()
	for row in query_rows:
		print(row)
	cur.close()
	db.close()