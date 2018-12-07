import sqlite3
conn =sqlite3.connect("mydatabase.db")
c=conn.cursor()

#c.execute("CREATE TABLE MytestDB (name text, rollno integer, course text)")

c.execute("insert into MytestDB VALUES (?,?,?)",("suyash",23,"it"))
conn.commit()

c.execute("select * from MytestDB")
conn.commit()
print(c.fetchall())


conn.commit()
conn.close()
