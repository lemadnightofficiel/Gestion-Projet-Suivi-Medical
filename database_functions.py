import sqlite3
from datetime import date

def send_to_medicalinfo_db(medical_values,username):
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=?", username)
    userID = cursor.fetchall()
    date = date.today()
    all_values =  (userID,date)
    for value in medical_values:
        all_values.append(value)
    cursor.execute("INSERT INTO medicalinfo (userID, date, height, weight, bpm, oxy_sat, tas, tad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", all_values)
    connection.commit() # apply modifications to the database when finnished
    connection.close() # faut pas un bac+5 pour comprendre cette ligne
    return None