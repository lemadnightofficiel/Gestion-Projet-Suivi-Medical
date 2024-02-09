import sqlite3

connection = sqlite3.connect("pulse_report.db")
cursor = connection.cursor()

User_values = [
('Jeremy',  'Gaudin', True, '2005-05-03', 'jeremy', 'jeremy'),
('Matthieu', 'Caron', True, '2005-05-25', 'matthieu', 'matthieu'),
('Najm', 'Adam', True, '2000-07-08', 'najm', 'najm'),
]

Medical_values = [
(1, '2024-02-06', 175, 73, 80, 97, 112, 68),
(1, '2024-02-07', 174, 74, 78, 98, 105, 67),
(1, '2024-02-08', 176, 76, 83, 98, 110, 69),
(2, '2024-02-06', 60, 13, 80, 97, 60, 20),
(2, '2024-02-07', 70, 20, 78, 98, 78, 32),
(2, '2024-02-08', 70, 20, 83, 98, 78, 32),
]

cursor.executemany("INSERT INTO users (name, lastname, sex, birthday, username, password) VALUES (?, ?, ?, ?, ?, ?)", User_values) # execute many times the command until all values are sent
cursor.executemany("INSERT INTO medicalinfo (userID, date, height, weight, bpm, oxy_sat, tas, tad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", Medical_values)

connection.commit() # apply modifications to the database when finnished

cursor.execute("SELECT * FROM users")
user = cursor.fetchall() # get all results from the command executed
print(user)

cursor.execute("SELECT * FROM medicalinfo")
medical = cursor.fetchall() # get all results from the command executed
print(medical)


connection.close() # faut pas un bac+5 pour comprendre cette ligne