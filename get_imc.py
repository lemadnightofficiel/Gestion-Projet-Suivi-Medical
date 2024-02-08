import sqlite3
from datetime import datetime
from check_imc import get_imc
from graph_functions import imc_graph

def get_imc_values(username):
    connection = sqlite3.connect("medical_info.db")
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
    imc_graph(imc_date) 
    return None

get_imc_values("Jeremy")