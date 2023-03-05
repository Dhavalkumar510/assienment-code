import pandas as pd
import matplotlib.pyplot as plt

"""
pandas and matplot are mathematical modules
here both are used as short form
"""

"""

"""
def lineplot(data, a1, b1, c1, d1, e1, f1):
    """
    

    Parameters
    ----------
    data :  data is one type of file like csv, xsls and etc and it's important
           to import values for required chart or graph
    a1 : a1 represents arguments of data which is useful to make plot 
    b1 : b1 represents arguments of data which is useful to make plot
    c1 : c1 represents arguments of data which is useful to make plot
    d1 : d1 represents arguments of data which is useful to make plot
    e1 : e1 represents arguments of data which is useful to make plot
    f1 : f1 represents arguments of data which is useful to make plot
    Returns
    -------
    None.

    """
    
    plt.figure(figsize=(8, 4))
    plt.title("NO. OF REGISTERED VEHICLES", size = 25)
    plt.xlabel("Year", size = 20)
    plt.tick_params(axis='y', labelrotation=45)
    plt.ylabel("No. of Vehicles", size = 20)
    plt.plot(data["Year"], data[a1], "k--", label=a1)
    plt.plot(data["Year"], data[b1], "r-", label=b1)
    plt.plot(data["Year"], data[c1], "bD", label=c1)
    plt.plot(data["Year"], data[d1], "g:", label=d1)
    plt.plot(data["Year"], data[e1], "c-.", label=e1)
    plt.plot(data["Year"], data[f1], "mx", label=f1)
    plt.legend(loc="upper left")
    
    plt.savefig('lineplot.png') 
    # Save the plot to file using savefig() method
       
    plt.show()
    
    """
    "mx" shows x tilted cross line with magenta color
    "c-." represents dash-dot line style like '-.' with given cyan color
    "g:" shows dotted line style like ':' with green color 
    "bD" represents diamond line with blue color
    "r-" shows solid line style with red color
    "k--" shows dashed line style like '--' with black color
    """
    
    """
    The function has a figure with the title, xlabel, and ylabel.
    It plots each variable against the year using different line styles.
    The plt.legend() function is used to add a legend to the plot with given location.
    """
    
data = pd.read_csv("C:/Users/User/Desktop/Annex_2.1_RTYB_1951-2015.csv")

# Example of lineplot
lineplot(data.iloc[28:], "All Vehicles", "Two Wheelers",
         "Cars, Jeeps and Taxis", "Buses", "Goods Vehicles", "Others")

"""
above lineplot() is a function 
"""
