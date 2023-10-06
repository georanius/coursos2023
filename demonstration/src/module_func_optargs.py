# example calculating change in sea ice extent from data points

import numpy as np

def Plotarray_with_title(data, titel='SET TITLE', label=None):
    """ Plotting function of 2-D array like a f(x), first is x and second is f(x),  """
    
    import matplotlib.pyplot as plt # as local as possible, as global as necessary
    
    plt.plot(data[:,1],data[:,0],'D-', label=label)
    plt.xlabel(titel)
    plt.ylabel(label)
    plt.title(titel)
    plt.grid(True)
    plt.legend();
    
    return data
