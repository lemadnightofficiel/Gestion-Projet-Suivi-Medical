import sqlite3

connection = sqlite3.connect("medical_info.db")
cursor = connection.cursor()

User_values = [
('Jeremy',  'Gaudin'),
('Matthieu', 'Caron'),
('Najm', 'Adam'),
]

Medical_values = [
('1', '2006-5-2', '60', '13', '140', '97', '60', '20'),
('1', '2007-5-2', '70', '20', '160', '98', '78', '32'),
('2', '2007-5-2', '70', '20', '160', '98', '78', '32'),
]

cursor.execute("DROP TABLE IF EXISTS users") # send command to the database 
cursor.execute("DROP TABLE IF EXISTS medicalinfo")

cursor.execute("CREATE TABLE users (userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(32), lastname VARCHAR(32), sex BOOL, birthday DATE, username VARCHAR(64) UNIQUE, password VARCHAR(64))")
cursor.execute("CREATE TABLE medicalinfo (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, userID INTEGER NOT NULL, date DATE, height SMALLINT(300), weight SMALLINT(635), bpm TINYINT, oxy_sat TINYINT(100), tas TINYINT, tad TINYINT, FOREIGN KEY (userID) REFERENCES users(userID))") # send command to the database

cursor.executemany("INSERT INTO users (name, lastname) VALUES (?, ?)", User_values) # execute many times the command until all values are sent
cursor.executemany("INSERT INTO medicalinfo (userID, date, height, weight, bpm, oxy_sat, tas, tad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", Medical_values)

connection.commit() # apply modifications to the database when finnished

cursor.execute("SELECT name FROM users")
user = cursor.fetchall() # get all results from the command executed
print(user)

cursor.execute("SELECT * FROM medicalinfo")
medical = cursor.fetchall() # get all results from the command executed
print(medical)

cursor.execute("SELECT users.name, users.lastname, medicalinfo.height, medicalinfo.weight FROM medicalinfo INNER JOIN users ON medicalinfo.userID = users.userID WHERE users.name = 'Jeremy'")
medical = cursor.fetchall() # get all results from the command executed
print(medical)

connection.close() # faut pas un bac+5 pour comprendre cette ligne