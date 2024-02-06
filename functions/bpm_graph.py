import matplotlib.pyplot as plt
from datetime import datetime

def bpm_graph():

    x = [1,2,3,4,5,6]
    y = [80,92,87,78,96,100]

    plt.plot(x, y, label= "BPM", color= "orange", linestyle='-')
    plt.xlabel('Dates')
    plt.ylabel('BPM')
    plt.title('Suivi de votre BPM :')
    plt.legend()
    
    time = datetime.now().strftime("%H%M%d%m%Y")
    plt.savefig(f"assets/bpm_graph/graph_{time}.png")

bpm_graph()
