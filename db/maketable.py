import psycopg2

conn = psycopg2.connect(database="sent", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#First step, create a cursor

cur = conn.cursor()
cur.execute('''CREATE TABLE tweets
	(ID SERIAL PRIMARY KEY NOT NULL,
	username TEXT NOT NULL,
	tweet TEXT  NOT NULL,
	time TIMESTAMP NOT NULL,
	location TEXT,
	pos FLOAT NOT NULL,
	neu FLOAT NOT NULL,
	neg FLOAT NOT NULL,
	compound FLOAT NOT NULL);''')
conn.commit()
conn.close()
