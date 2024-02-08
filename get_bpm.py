import sqlite3
from datetime import datetime
from graph_functions import bpm_graph

def get_bpm_values(username):
    connection = sqlite3.connect("medical_info.db")
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE name=?", [username])
    userID = cursor.fetchall()[0]
    cursor.execute("SELECT medicalinfo.bpm, medicalinfo.oxy_sat, medicalinfo.date, users.sex FROM medicalinfo INNER JOIN users ON medicalinfo.userID = users.userID WHERE users.userID=?", userID)
    data_list = cursor.fetchall()

    bpm_date = []

    for data in data_list:
        data = list(data)
        data[2] = datetime.strptime(data[2], '%Y-%m-%d').strftime('%d-%m-%Y')
        bpm_date.append(data)
    bpm_graph(bpm_date) 
    return None

get_bpm_values("Jeremy")