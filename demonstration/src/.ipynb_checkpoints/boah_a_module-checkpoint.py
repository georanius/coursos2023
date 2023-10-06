# example calculating change in sea ice extent from data points

import numpy as np

def seaice_change(extent):
    """ HERE IS A PROVUND AND COMPREHENCIVE FUNKTION DESCRIPTION: extent is an one-dim. array with time-ordered values for sea ice extent """
    
    import matplotlib.pyplot as plt # as local as possible, as global as necessary
    
    plt.plot(extent,'D-', label='DATA-TYPE')
    plt.xlabel('Time')
    plt.ylabel('extent [unit]')
    plt.title('TITLE')
    plt.grid(True)
    plt.legend();
    
    begin = extent[0]
    today = extent[-1]
    change = np.round(today - begin,3)
    perc = np.round(change/begin,2)
    return change, perc*100
