#this is a nice module file containing usefull this comment
# and a class 
# you my import it as(import NiceModuleName as KurzMoNa) or 

import numpy
import random
import matplotlib.pyplot as plt
import pylab

class SuperHero:  # new class called 'SuperHero'
    
    # Initializer of object/instance; 
    #__init__() function to assign values to object properties... python flavour
    def __init__(self, name):
        #body of constructor
        self.name = name
        
    def makes_super_action(self):
        # defining the number of steps
        n = 10000

        #creating two array for containing x and y coordinate
        #of size equals to the number of size and filled up with 0's
        x = numpy.zeros(n)
        y = numpy.zeros(n)

        # filling the coordinates with random variables
        for i in range(1, n):
            val = random.randint(1, 4)
            if val == 1:
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
            elif val == 2:
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
            elif val == 3:
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
            else:
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 2


        # plotting stuff:
        pylab.title("Buy this master piece in our shop")
        pylab.plot(x, y)
        #pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
        pylab.show()

        
    
        
        