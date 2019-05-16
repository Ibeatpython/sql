import sqlite3


with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	cities = [('Boston', 'MA', 1000000),
	('San Jose', 'CA', 1200000),
	('Jacksonville', 'FL', 800000),
	('Austin', 'TX', 700000)]
	c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)
	c.execute("SELECT * FROM population WHERE population > 1000000")
	rows = c.fetchall()
	for r in rows:
		print(r)


with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE regions(city TEXT, region TEXT)")
	city = [('NEW YORK CITY','Notheast'), ('Los Angeles', 'West'),
	('Houston', 'South'), ('Philadelphia', 'Northeast'), ('San Antonio', 'South'),
	('San Diego', 'West'),('Dallas', 'South'),('San Jose', 'West'),('Jacksonville', 'South'), 
	('Indianapolis', 'Midwest'), ('Austin', 'South'),('Detroit', 'Midwest')]
	c.executemany("INSERT INTO regions VALUES(?,?)", city)
	c.execute("SELECT * FROM regions ORDER BY region")
	rows = c.fetchall()
	for r in rows:
		print(r)



with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("""SELECT population.city, population.population, regions.region from population, 
	regions WHERE population.city = regions.city""")
	rows = c.fetchall()
	for r in rows:
		print("city:" + r[0])
		print("population:" + str(r[1]))
		print("regions:" + r[2])
		print("")


