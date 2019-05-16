

import sqlite3
import csv

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("SELECT city, state FROM population")
	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1])


