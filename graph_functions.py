import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import os

def bpm_graph(data_list): #To display a BPM graph
    
    time = datetime.now().strftime("%Y-%m-%d") #Set the time
    
    if os.path.isfile(f"static/graph/bpm_graph_{time}.png"): #Check if the existing file 
        os.remove(f"static/graph/bpm_graph_{time}.png") #Delete to replace the file with an other image
    
    bpm_fig = plt.figure("BPM") #Create a figure for avoid the elements accumulation in the graph

    x = []
    y = []

    for data in data_list: #Append data
        x.append(data[1])
        y.append(data[0])

    plt.plot(x, y, label= "BPM", color= "red", linestyle='-') #Draw the curve
    plt.ylabel("BPM")
    plt.title('Suivi de votre BPM :')

    plt.savefig(f"static/graph/bpm_graph_{time}.png") #Save the file with the date
    return f"../static/graph/bpm_graph_{time}.png"

def oxysat_graph(data_list): #To display an oxygen saturation graph

    time = datetime.now().strftime("%Y-%m-%d") #Set the time

    if os.path.isfile(f"static/graph/oxysat_graph_{time}.png"):  #Check if the existing file
        os.remove(f"static/graph/oxysat_graph_{time}.png") #Delete to replace the file with an other image
    
    oxysat_fig = plt.figure("OxySat")  #Create a figure for avoid the elements accumulation in the graph

    x = []
    y = []

    for data in data_list: #Append data
        x.append(data[1])
        y.append(data[0])

    plt.plot(x, y, label= "Saturation en oxygène", color= "blue", linestyle='-') #Draw the curve
    plt.xlabel("Dates")
    plt.ylabel("Saturation oxygène")
    plt.title('Suivi de votre saturation en oxygène :')

    plt.savefig(f"static/graph/oxysat_graph_{time}.png") #Save the file with the date
    return f"../static/graph/oxysat_graph_{time}.png"

def imc_graph(data_list): #To display an imc graph

    time = datetime.now().strftime("%d-%m-%Y") #Set the time

    if os.path.isfile(f"static/graph/imc_graph_{time}.png"): #Check if the existing file
        os.remove(f"static/graph/imc_graph_{time}.png") #Delete to replace the file with an other image

    imc_fig = plt.figure("IMC") #Create a figure for avoid the elements accumulation in the graph

    x = []
    y = []

    for data in data_list: #Append Data
        x.append(data[1])
        y.append(data[0])

    plt.plot(x, y, label= "IMC", color= "green", linestyle='-') #Draw the curve
    plt.xlabel("Dates")
    plt.ylabel("IMC")
    plt.title('Suivi de votre IMC :')

    plt.savefig(f"static/graph/imc_graph_{time}.png") #Save the file with the date
    return f"../static/graph/imc_graph_{time}.png"

def pressure_graph(data_list): #To display a pressure graph

    time = datetime.now().strftime("%Y-%m-%d") #Set the time
    
    if os.path.isfile(f"static/graph/pressure_graph_{time}.png"): #Check if the existing file
        os.remove(f"static/graph/pressure_graph_{time}.png") #Delete to replace the file with an other image

    pressure_fig = plt.figure("Pressure") #Create a figure for avoid the elements accumulation in the graph

    systolique = []
    diastolique = []
    dates = []

    for data in data_list: #Append Data
        systolique.append(data[0])
        diastolique.append(data[1])
        dates.append(data[2])

    plt.plot(dates, systolique, label= "Pression systolique", color= "red", linestyle='-') #Draw the curve
    plt.plot(dates, diastolique, label= "Pression diastolique", color= "blue", linestyle='-') #Draw the other curve
    plt.xlabel("Dates")
    plt.ylabel("Pressions cardiovasculaires")
    plt.title('Suivi de votre Tension :')

    plt.savefig(f"static/graph/pressure_graph_{time}.png") #Save the file with the date
    return f"../static/graph/pressure_graph_{time}.png"

def delete_allgraph():
    for graph in os.listdir('static/graph'):
        if os.path.isfile(os.path.join('static/graph', graph)):
            os.remove(os.path.join('static/graph', graph))
