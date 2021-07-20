import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5431'
)
#Creating a cursor object using the cursor() method

abcd="abc"
pqr="Mumbai"
cursor = conn.cursor()
sql = "INSERT INTO candidate_v (fname, location) VALUES ('"+abcd+"','"+pqr+"')"
cursor.execute(sql)
conn.commit()
print("Table created successfully........")

#Closing the connection

conn.close()
