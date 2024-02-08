import sqlite3
from datetime import datetime
from check_imc import get_imc
import graph_functions

def get_bpm_values(username):
    connection = sqlite3.connect("pulse_report.db")
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
    graph_functions.bpm_graph(bpm_date) 
    return None

def get_imc_values(username):
    connection = sqlite3.connect("pulse_report.db")
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE name=?", [username])
    userID = cursor.fetchall()[0]
    cursor.execute("SELECT height, weight, date FROM medicalinfo WHERE userID=?", userID)
    data_list = cursor.fetchall()

    imc_date = []
    for data in data_list:
        imc = get_imc(data[0],data[1])
        data = list(data)
        data[0] = imc
        data[2] = datetime.strptime(data[2], '%Y-%m-%d').strftime('%d-%m-%Y')
        data.pop(1)
        imc_date.append(data)
    graph_functions.imc_graph(imc_date) 
    return None

def get_pressure_values(username):
    connection = sqlite3.connect("pulse_report.db")
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
    graph_functions.pressure_graph(pressure_date) 
    return None


get_bpm_values('jeremy')
get_imc_values('jeremy')
get_pressure_values('jeremy')