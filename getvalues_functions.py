import sqlite3
from datetime import datetime
import graph_functions

def get_bpm_values(username): #To get the BPM
    connection = sqlite3.connect("pulse_report.db") #Database connection
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=?", [username]) #Send SQL command to get the userID 
    userID = cursor.fetchall()[0]
    cursor.execute("SELECT medicalinfo.bpm, medicalinfo.date, users.sex FROM medicalinfo INNER JOIN users ON medicalinfo.userID = users.userID WHERE users.userID=?", userID) #To get necessary informations to return the BPM
    data_list = cursor.fetchall() #To get informations

    bpm_date = []
    for data in data_list: #For loop to replace informations and change the date
        data = list(data)
        data[2] = datetime.strptime(data[2], '%Y-%m-%d').strftime('%d-%m-%Y')
        bpm_date.append(data)
    return graph_functions.bpm_graph(bpm_date) 

def get_oxysat_values(username): #To get the oxygen saturation
    connection = sqlite3.connect("pulse_report.db")
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=?", [username])
    userID = cursor.fetchall()[0]
    cursor.execute("SELECT oxy_sat, date FROM medicalinfo WHERE userID=?", userID)
    data_list = cursor.fetchall()

    oxysat_date = []
    for data in data_list:
        data = list(data)
        data[1] = datetime.strptime(data[1], '%Y-%m-%d').strftime('%d-%m-%Y')
        oxysat_date.append(data) 
    return graph_functions.oxysat_graph(oxysat_date) 

def get_imc_values(username): #To get the imc 
    connection = sqlite3.connect("pulse_report.db")
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=?", [username])
    userID = cursor.fetchall()[0]
    cursor.execute("SELECT height, weight, date FROM medicalinfo WHERE userID=?", userID)
    data_list = cursor.fetchall()

    imc_date = []
    for data in data_list: #For loop to replace elements and add IMC to the data
        imc = get_imc(data[0],data[1])
        data = list(data)
        data[0] = imc
        data[2] = datetime.strptime(data[2], '%Y-%m-%d').strftime('%d-%m-%Y')
        data.pop(1)
        imc_date.append(data)
    return graph_functions.imc_graph(imc_date)

def get_pressure_values(username): #To get the blood pressure
    connection = sqlite3.connect("pulse_report.db")
    cursor = connection.cursor()
    cursor.execute("SELECT userID FROM users WHERE username=?", [username]) 
    userID = cursor.fetchall()[0]
    cursor.execute("SELECT tas, tad, date FROM medicalinfo WHERE userID=?", userID)
    data_list = cursor.fetchall()

    pressure_date = []
    for data in data_list:
        data = list(data)
        data[2] = datetime.strptime(data[2], '%Y-%m-%d').strftime('%d-%m-%Y')
        pressure_date.append(data)
    return graph_functions.pressure_graph(pressure_date)

def get_imc(weight, height): #To calculate the IMC
    weight = float(weight) # kg
    height = float(height*0.1) # cm
    imc = (weight/(height*height))
    return imc
