import matplotlib.pyplot as plt
from datetime import datetime
import os

def bpm_graph(data_list):
    
    time = datetime.now().strftime("%Y-%m-%d")

    if os.path.isfile(f"static/images/bpm_graph_{time}.png"):
        os.remove(f"static/images/bpm_graph_{time}.png")
    
    bpm_fig = plt.figure("BPM")

    x = []
    y = []

    for data in data_list:
        x.append(data[2])
        y.append(data[0])

    plt.plot(x, y, label= "BPM", color= "red", linestyle='-')
    plt.ylabel("BPM")
    plt.title('Suivi de votre BPM :')
    plt.legend()

    plt.savefig(f"static/images/bpm_graph_{time}.png")
    return f"../static/images/bpm_graph_{time}.png"

def oxysat_graph(data_list):

    time = datetime.now().strftime("%Y-%m-%d")

    if os.path.isfile(f"static/images/oxysat_graph_{time}.png"):
        os.remove(f"static/images/oxysat_graph_{time}.png")
    
    oxysat_fig = plt.figure("OxySat")

    x = []
    y = []

    for data in data_list:
        x.append(data[1])
        y.append(data[0])

    plt.plot(x, y, label= "Saturation en oxygène", color= "blue", linestyle='-')
    plt.xlabel("Dates")
    plt.ylabel("Saturation oxygène")
    plt.title('Suivi de votre saturation en oxygène :')
    plt.legend()

    plt.savefig(f"static/images/oxysat_graph_{time}.png")
    return f"../static/images/oxysat_graph_{time}.png"

def imc_graph(data_list):

    time = datetime.now().strftime("%d-%m-%Y")

    if os.path.isfile(f"static/images/imc_graph_{time}.png"):
        os.remove(f"static/images/imc_graph_{time}.png")

    imc_fig = plt.figure("IMC")

    x = []
    y = []

    for data in data_list:
        x.append(data[1])
        y.append(data[0])

    plt.plot(x, y, label= "IMC", color= "green", linestyle='-')
    plt.xlabel("Dates")
    plt.ylabel("IMC")
    plt.title('Suivi de votre IMC :')
    plt.legend()

    plt.savefig(f"static/images/imc_graph_{time}.png")
    return f"../static/images/imc_graph_{time}.png"

def pressure_graph(data_list):

    time = datetime.now().strftime("%Y-%m-%d")
    
    if os.path.isfile(f"static/images/pressure_graph_{time}.png"):
        os.remove(f"static/images/pressure_graph_{time}.png")

    pressure_fig = plt.figure("Pressure")

    systolique = []
    diastolique = []
    dates = []

    for data in data_list:
        systolique.append(data[0])
        diastolique.append(data[1])
        dates.append(data[2])

    plt.plot(dates, systolique, label= "Pression systolique", color= "red", linestyle='-')
    plt.plot(dates, diastolique, label= "Pression diastolique", color= "blue", linestyle='-')
    plt.xlabel("Dates")
    plt.ylabel("Pressions cardiovasculaires")
    plt.title('Suivi de votre Tension :')
    plt.legend()

    plt.savefig(f"static/images/pressure_graph_{time}.png")
    return f"../static/images/pressure_graph_{time}.png"
