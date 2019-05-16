import sqlite3
with sqlite3.connect("new.db") as connections:
	c = connections.cursor()
	c.execute("CREATE TABLE inventory (vehicle TEXT, model TEXT, quantity INT)")
	vehicles = [('Ford', 'FIESTA', 5),('Ford', 'FUSION', 2),('Ford', 'MUSTIAN', 9),
	('Honda', 'Insight', 3),('Honda', 'Accord', 5)]
	c.executemany("INSERT INTO inventory (vehicle, model, quantity) values(?, ?, ?)", vehicles)
