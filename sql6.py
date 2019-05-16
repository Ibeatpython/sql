import sqlite3
conn = sqlite3.connect("new.db")
c = conn.cursor()
c.execute("UPDATE inventory SET quantity=5 WHERE model='FUSION' or model='Insight'")
conn.commit()
conn.close()