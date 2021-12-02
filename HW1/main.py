import matplotlib.pyplot as plt
import numpy as np

def y(x):
    cube = pow(x,3)
    sqr= pow (x,2)
    return cube-3*0.06*sqr+4*0.000216*0.55

def findError(prev,new):
    numerator=abs(new-prev)
    denominator=new
    return (numerator/denominator)*100

def getMid(a,b):
    return (a+b)/2

def generateInputs(lowerBound,upperBound,step):
    return np.arrange(lowerBound,upperBound,step)

def plotGraph():
    xValues=generateInputs(-3,3,1)
    yValues=[]

    for i in range(20):
        tempY=y(xValues[i-1])
        yValues.append(tempY)

    plt.plot(xValues,yValues,marker="o")
    plt.show()

def doBisectionMethod(lowerBound,upperBound,error,maxIteration):
    #Hello
    
    return 9
plotGraph()