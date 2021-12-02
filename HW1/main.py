import matplotlib.pyplot as plt
import numpy as np

def y(x):
    cube = pow(x,3)
    sqr= pow (x,2)
    return cube-3*0.06*sqr+4*0.000216*0.55

def findError(prev,new):
    numerator=abs(abs(new)-abs(prev))
    denominator=new
    return (numerator/denominator)*100

def getMid(a,b):
    return (a+b)/2

def generateInputs(lowerBound,upperBound,step):
    return(np.arange(lowerBound,upperBound,step))

def plotGraph(xValues):
    
    yValues=[]

    for i in xValues:
        tempY=y(i)
        yValues.append(tempY)

    plt.plot(xValues,yValues,marker="o")
    plt.show()

def doBisectionMethod(lowerBound,upperBound,error=0.5,maxIteration=20):
    fLower=y(lowerBound)
    fUpper=y(upperBound)
    for i in range(maxIteration):
        mid=(upperBound+lowerBound)/2
        oldMid=0
        if (y(mid)*y(upperBound)<0):
            oldMid=lowerBound
            lowerBound=mid 
            
        elif(y(mid)*y(lowerBound)<0): 
            oldMid=upperBound
            upperBound=mid
            
        
        currentError=findError(oldMid,mid)
        print("lower ",lowerBound," upper ",upperBound,"mid ",mid)
        print("Error  : ",currentError)
        
    return 9

xValues=generateInputs(-3,3,0.3)
#plotGraph(xValues)
doBisectionMethod(-3,3.1)