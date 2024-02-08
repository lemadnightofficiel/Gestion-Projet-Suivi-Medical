import sqlite3

connection = sqlite3.connect("pulse_report.db")
cursor = connection.cursor()

User_values = [
('Jeremy',  'Gaudin', True, '2005-05-03', 'jeremy', 'jeremy'),
('Matthieu', 'Caron', True, '2005-05-25', 'matthieu', 'matthieu'),
('Najm', 'Adam', True, '2000-07-08', 'najm', 'najm'),
]

Medical_values = [
(1, '2024-02-06', 60, 13, 80, 97, 60, 20),
(1, '2024-02-07', 70, 20, 78, 98, 78, 32),
(2, '2024-02-07', 70, 20, 83, 98, 78, 32),
]

cursor.execute("DROP TABLE IF EXISTS users") # send command to the database 
cursor.execute("DROP TABLE IF EXISTS medicalinfo")

cursor.execute("CREATE TABLE users (userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(32), lastname VARCHAR(32), sex BOOL NOT NULL, birthday DATE NOT NULL, username VARCHAR(64) UNIQUE NOT NULL, password VARCHAR(64))")
cursor.execute("CREATE TABLE medicalinfo (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, userID INTEGER NOT NULL, date DATE, height SMALLINT(300), weight SMALLINT(635), bpm SMALLINT, oxy_sat TINYINT(100), tas SMALLINT, tad SMALLINT, FOREIGN KEY (userID) REFERENCES users(userID))") # send command to the database

cursor.executemany("INSERT INTO users (name, lastname, sex, birthday, username, password) VALUES (?, ?, ?, ?, ?, ?)", User_values) # execute many times the command until all values are sent
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