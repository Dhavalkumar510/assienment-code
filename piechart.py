import pandas as pd
import matplotlib.pyplot as plt

"""
pandas and matplot are mathematical modules which are very usefull to make
code very easy in python 
"""

x = pd.read_csv("C:/Users/User/Desktop/piechart.csv")
print(x)
def piechart():
    """
    Creates a pie chart with given parameters
    Creates a 2x2 grid of pie charts using the data in x.
    Returns
    -------
    None.

    """
    # create a subplot of size 2x2
    fig=plt.figure(figsize=(20, 20), dpi= 100, facecolor='w', 
                   edgecolor='k')
    fig, axs = plt.subplots(2, 2)
    
    """
    plot the graph of 1951, 1975, 2000, 2015 according to their data
    """
    axs[0, 0].pie(x["1951"], labels = x["Year"], 
            explode=[0.040] * len(x["Year"]))
    axs[0, 0].set_title('1951')


    axs[0, 1].pie(x["1975"], labels = x["Year"], 
            explode=[0.030] * len(x["Year"]))
    axs[0, 1].set_title('1975')


    axs[1, 0].pie(x["2000"], labels = x["Year"], 
            explode=[0.025] * len(x["Year"]))
    axs[1, 0].set_title('2000')


    axs[1, 1].pie(x["2015"], labels = x["Year"], 
            explode=[0.040] * len(x["Year"]))
    axs[1, 1].set_title('2015')
    
    plt.savefig("piechart.png")
    for ax in axs.flat:
        ax.set()
        
# we are using function for present a piechart
#Example
piechart()





    
