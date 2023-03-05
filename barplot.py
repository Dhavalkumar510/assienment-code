import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
pandas and matplot are mathematical modules which are very usefull to make
code very easy in python 
numpy is numerical mathematical package for python
"""

def barplot():
    """
    plotting barplot using different parameters

    Returns
    -------
    None.

    """
    plt.figure(figsize=(20, 10))
    N = 8
    ind = np.arange(N)
    width = 0.25
    
    """
    plot 3 barplot e.g. bar1, bar2, bar3
    """
    xvals = x["1990 [YR1990]"]
    bar1 = plt.bar(ind, xvals, width, color = 'y')

    yvals = x["2000 [YR2000]"]
    bar2 = plt.bar(ind+width, yvals, width, color='g')

    zvals = x["2010 [YR2010]"]
    bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')
    
    """plot the labels, title and different parameters for given barplot
    """

    plt.xlabel("country", size = 20)
    plt.ylabel("Ratio in percentage(%)", size = 15)
    plt.title("Ratio of female to male \n labor force participation rate", 
              size = 30)

    plt.xticks(ind+width, x["Country Name"])
    plt.xticks(minor = False, ha = "right")
    plt.tick_params(axis='x', labelsize = 15, labelrotation = 15)
    plt.tick_params(axis='y', labelsize = 30)
    plt.legend((bar1, bar2, bar3), ('1990', '2000', '2010'),
               prop = {"size":25})
    plt.savefig("barplot.png")
    
""" Example for barplot
"""
x = pd.read_csv("C:/Users/User/Desktop/pie.csv")
barplot()
