import sqlite3

'''
Creates the empty database
If the database already exists, this programm empties the database 

!YOU NEED TO RUN THE PROGRAM AT LEAST ONCE BEFORE LAUNCHING THE APP!
'''

# Creates the sqlite database pulse_report if it doesnt exist already
# Connects to the database
connection = sqlite3.connect("pulse_report.db")
cursor = connection.cursor() # We position ourselves in the database via a cursor

# If the database already exists, we delete both tables
cursor.execute("DROP TABLE IF EXISTS users") 
cursor.execute("DROP TABLE IF EXISTS medicalinfo")

# We create 2 tables, users and medicalinfo and specify the columns along with the primary and foreign keys if there are any
cursor.execute("CREATE TABLE users (userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(32), lastname VARCHAR(32), sex BOOL NOT NULL, birthday DATE NOT NULL, username VARCHAR(64) UNIQUE NOT NULL, password VARCHAR(64) NOT NULL)") # send command to the database
cursor.execute("CREATE TABLE medicalinfo (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, userID INTEGER NOT NULL, date DATE, height SMALLINT(300), weight SMALLINT(635), bpm SMALLINT, oxy_sat TINYINT(100), tas SMALLINT, tad SMALLINT, FOREIGN KEY (userID) REFERENCES users(userID))") # send command to the database

connection.commit() # apply modifications to the database when finnished
connection.close() # faut pas un bac+5 pour comprendre cette ligne