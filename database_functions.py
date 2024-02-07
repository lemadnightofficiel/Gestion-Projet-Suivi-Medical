import sqlite3
from datetime import date

def send_to_medicalinfo_db(medical_values,username):
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=?", [username])
    userID = cursor.fetchall()[0][0]
    today = str(date.today())
    height,weight,bpm,oxy_sat,tas,tad = medical_values
    cursor.execute("INSERT INTO medicalinfo (userID, date, height, weight, bpm, oxy_sat, tas, tad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (userID, today, height, weight, bpm, oxy_sat, tas, tad))
    connection.commit() # apply modifications to the database when finnished
    connection.close() # faut pas un bac+5 pour comprendre cette ligne
    return None

def check_user(username):
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users WHERE username=?", [username])
    user = cursor.fetchall()
    connection.close()
    if len(user) == 0 :
        return False
    else:
        return True
    
def check_date(username):
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    info = [username,date.today()]
    cursor.execute("SELECT medicalinfo.id FROM medicalinfo INNER JOIN users ON medicalinfo.userID = users.userID WHERE users.username=? AND medicalinfo.date=?", info)
    user = cursor.fetchall()
    connection.close()
    if len(user) == 0 :
        return False
    else:
        return True
