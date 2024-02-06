import matplotlib.pyplot as plt
from datetime import datetime

def bpm_graph():

    dates = [1,2,3,4,5]
    systolique = [111,113,115,118,120]
    diastolique = [79,80,82,84,88]

    plt.plot(dates, systolique, label= "Pression systolique", color= "red", linestyle='-')
    plt.plot(dates, diastolique, label= "Pression diastolique", color= "blue", linestyle='-')
    plt.xlabel('Dates')
    plt.ylabel('BPM')
    plt.title('Suivi de votre Tension :')
    plt.legend()
    
    time = datetime.now().strftime("%H%M%d%m%Y")
    plt.savefig(f"assets/pressure_graph/graph_{time}.png")

bpm_graph()
