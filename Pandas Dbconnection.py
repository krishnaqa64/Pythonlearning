import pandas as pd

import sqlite3
conn=sqlite3.connect("customer.db")
c=conn.cursor()

# c.execute("""
# CREATE TABLE contacts (
# 	contact_id INTEGER PRIMARY KEY,
# 	first_name TEXT NOT NULL,
# 	last_name TEXT NOT NULL,
# 	email TEXT NOT NULL UNIQUE,
# 	phone TEXT NOT NULL UNIQUE
# )""")
# c.execute("insert into contacts values (1,'kiran','raja','kiran_raja@gmail.com','647-945-2345')")
# c.execute("insert into contacts values (2,'raze','kala','raze_kala@gmail.com','647-946-2345')")

c.execute("select * from contacts")
result = c.fetchall()
print("result = ", result)


names= [x[0] for x in c.description]
print("names :- ",names)

resultset=list(map(lambda row: dict(zip(names,row)),result))

print(resultset)
conn.commit()
conn.close()

# while (1):
#     row = c.fetchone()
#     if row == None:
#         break
#     print ("%s %s %s\n" % (row[0], row[1], row[2]))