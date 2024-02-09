import sqlite3
from datetime import date


def send_to_medicalinfo_db(medical_values,username):
    '''
    Function: send_to_medicalinfo_db
    - Sends informations to medicalinfo table in pulse_report database
    --------
    params:
    - medical_values: list of all medical informations to add to the database
    - username: the username of the user where the informations are linked
    -------
    From the username, we collect the userID
    Get today's date
    Get all the info from the medical_values list
    Insert all the information into the medicalinfo table
    -------
    returns: None
    '''
    connection = sqlite3.connect("pulse_report.db") #Connect to the local database 
    cursor = connection.cursor() 
    cursor.execute("SELECT userID FROM users WHERE username=?", [username]) # get userID from username in users table
    userID = cursor.fetchall()[0][0]
    today = date.today() # get today's date
    height,weight,bpm,oxy_sat,tas,tad = medical_values
    cursor.execute("INSERT INTO medicalinfo (userID, date, height, weight, bpm, oxy_sat, tas, tad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (userID, today, height, weight, bpm, oxy_sat, tas, tad)) # insert new line with all the infos in the medicalinfo table
    connection.commit() # apply modifications to the database when finnished
    connection.close() # faut pas un bac+5 pour comprendre cette ligne
    return None

def send_to_users_db(name,lastname,sex,birthday,username,password):
    '''
    Function: send_to_users_db
    - Sends informations to users table in pulse_report database
    --------
    params:
    - The info of the new user that is about to be added to the users table in the database
    -------
    Connect to the pulse_report database
    Insert all the information into the users table
    Save the changes
    Close the connection
    -------
    returns: None
    '''
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, lastname, sex, birthday, username, password) VALUES (?, ?, ?, ?, ?, ?)", (name, lastname, sex, birthday, username, password))
    connection.commit() # apply modifications to the database when finnished
    connection.close()
    return None

def check_user(username):
    '''
    Function: check_users
    - checks if a user exists in the users table or not
    --------
    params:
    - The username of the user we want to check exists or not
    -------
    Send a request for the user with the matching username
    Collect the data
    Check if the data is empty or not
    -------
    returns:
    - Boolean: True if user exists, False if not
    '''
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users WHERE username=?", [username])
    user = cursor.fetchall() # get all results from the command executed
    connection.close()
    if len(user) == 0 :
        return False
    else:
        return True
    
def check_date(username):
    '''
    Function: check_date
    - checks if a user has done the medical form today or not
    --------
    params:
    - The username of the user we want to check 
    -------
    Send a request for the todays medical info from that user (using Inner Join to ask for the matching username and today's date)
    Collect the data
    Check if the data is empty or not
    -------
    returns:
    - Boolean: True if info exists, False if not
    '''
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    info = [username,date.today()]
    cursor.execute("SELECT medicalinfo.id FROM medicalinfo INNER JOIN users ON medicalinfo.userID = users.userID WHERE users.username=? AND medicalinfo.date=?", info)
    user = cursor.fetchall() # get all results from the command executed
    connection.close()
    if len(user) == 0 :
        return False
    else:
        return True

def check_password(username):
    '''
    Function: check_password
    - collects the user's password
    --------
    params:
    - The username of the user we want to get the password
    -------
    Check if the user exists in the database via the check_user
    Send a request for the user's password form the users table in the database
    -------
    returns:
    - Password of the user if the user exists
    - None if the user does not exists
    '''
    if check_user(username): 
        connection = sqlite3.connect("pulse_report.db") #Connect to local database
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        password = cursor.fetchall()[0][0] # get all results from the command executed
        connection.close()
        return password
    else:
        return None

def get_today_info(username):
    '''
    Function: get_today_info
    - collects all of the users medical info from today in the medicalinfo database
    --------
    params:
    - The username of the user we want to get the medical info
    -------
    Send a request for all of the user's medical info from both the users and medicalinfo table in the database
    -------
    returns:
    - Data: a list of all the medical info from today
    '''
    connection = sqlite3.connect("pulse_report.db") #Connect to local database
    cursor = connection.cursor()
    info = [username,date.today()]
    cursor.execute("SELECT medicalinfo.height, medicalinfo.weight, medicalinfo.bpm, medicalinfo.oxy_sat, medicalinfo.tas, medicalinfo.tad, users.sex, users.birthday FROM medicalinfo INNER JOIN users ON medicalinfo.userID = users.userID WHERE users.username=? AND medicalinfo.date=?", info)
    data = cursor.fetchall() # get all results from the command executed
    connection.close()
    return data[0]