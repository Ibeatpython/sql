
import sqlite3
	

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

cursor.execute("""INSERT INTO population VALUES('New York City', 'NY', 84000)""")
cursor.execute("""INSERT INTO population VALUES('San Fansisco', 'CA', 80000)""")

conn.commit()
conn.close()




