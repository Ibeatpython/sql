import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	cities = [
	('Boston', 'MA', 1000000),
	('Chicaco', 'IL', 2000000)
	]
	c.executemany('INSERT INTO population VALUES(?,?,?)', cities)
