import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1, 'FAITH KAREMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2, 'BOB KURIA',25,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3, 'JANE GATHONI',28,300000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4, 'MARY ANNE',38,290000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5, 'MARY KERUBO',39,220000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()