import sqlite3
from datetime import datetime
from graph_functions import pressure_graph

def get_pressure_values(username):
    connection = sqlite3.connect("medical_info.db")
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE name=?", [username])
    userID = cursor.fetchall()[0]
    cursor.execute("SELECT tas, tad, date FROM medicalinfo WHERE userID=?", userID)
    data_list = cursor.fetchall()

    pressure_date = []

    for data in data_list:
        data = list(data)
        data[2] = datetime.strptime(data[2], '%Y-%m-%d').strftime('%d-%m-%Y')
        pressure_date.append(data)
    pressure_graph(pressure_date) 
    return None

get_pressure_values("Jeremy")