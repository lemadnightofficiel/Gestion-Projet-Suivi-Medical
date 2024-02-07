# https://www.w3schools.com/python/python_mysql_getstarted.asp

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("")

sql = ""
val = ""

mycursor.execute(sql, val)

mydb.commit()