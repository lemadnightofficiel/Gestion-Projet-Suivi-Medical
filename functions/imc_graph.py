import matplotlib.pyplot as plt
from datetime import datetime

def imc_graph():

    x = [1,2,3,4,5,6]
    y = [17,17.5,18.5,19,19.2,19.5]

    plt.plot(x, y, label= "IMC", color= "green", linestyle='-')
    plt.xlabel("Dates")
    plt.ylabel("IMC")
    plt.title('Suivi de votre IMC :')
    plt.legend()

    time = datetime.now().strftime("%Y-%m-%d")
    plt.savefig(f"assets/imc_graph_{time}.png")

imc_graph()
