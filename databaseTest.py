import mysql.connector

conn = mysql.connector.connect(username='root', password='322002',host='localhost',database='capstone',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()