# 1905079 | Salman Sayeed


"""
The initial guess must be between 0 and 8 
because height cannot be more that diameter
"""

import numpy as np
import matplotlib.pyplot as plt

pi=3.1416
def y(x):
    return pi*(x**3)-12*pi*(x**2)+15

def y1(x):
    return 3*pi*(x**2)-24*pi*x

def generateError(old,new):
    numerator=abs(new-old)
    denominator=new
    return (numerator/denominator)*100

def generateNewApproximation(old,y,y1):
    # Checking for division by 0
    if(y1==0):
        print("DIVISION BY 0 NOT ALLOWED!")
        return
    return old-(y/y1)

def newtonRaphson(startingEstimate,maxIteration=20,maxError=0.05):
    oldEstimate=startingEstimate
    newEstimate=startingEstimate
    for i in range(maxIteration):
        newEstimate=generateNewApproximation(oldEstimate, y(newEstimate), y1(newEstimate))
        error=generateError(oldEstimate, newEstimate)
        print( "Iteration :",i, "Estimate :", newEstimate, "Error :",error )
        if(error<maxError): 
            return
        oldEstimate=newEstimate
    return
newtonRaphson(5,70,.0005)



#Testing the result using graph
#=======================================


# Zoomed in 0.62,0.65,0.001
xValues=np.arange(0,8,1)
yValues=[]
for i in xValues:
    yValues.append(y(i))
    
plt.plot(xValues,yValues,marker="o",color="orange")
plt.xlabel("Value of h (ft)")
plt.ylabel("y")
plt.title("Graph for solving h")
plt.grid()
plt.show()