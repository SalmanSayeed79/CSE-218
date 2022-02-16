import matplotlib.pyplot as plt
import numpy as np

def y(x):
    cube = pow(x,3)
    sqr= pow (x,2)
    return cube-3*0.06*sqr+4*0.000216*0.55

def findError(prev,new):
    numerator=abs(abs(new)-abs(prev))
    denominator=new
    return abs((numerator/denominator)*100)

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
    
    estimate=upperBound
    oldEstimate=upperBound
    
    if(fLower*fUpper<0):
        print("Correct range chosen")
        
    #Returning if range is false
    else:
        print("Wrong range chosen")
        return
    
    for i in range(maxIteration):
        if (y(estimate)*y(lowerBound)>0):
            oldEstimate=estimate
            lowerBound=estimate 
            
        elif(y(estimate)*y(lowerBound)<0): 
            oldEstimate=estimate
            upperBound=estimate
        
        elif(y(estimate)==y(lowerBound)):
            return estimate
        
        estimate=(upperBound+lowerBound)/2
        currentError=findError(oldEstimate,estimate)
        
        #Debugging print
        # print("lower ",lowerBound," upper ",upperBound,"Estimate ",estimate)
        # print("Error  : ",currentError)
        
        #Returning if error found
        if(currentError<=error):
            print("Got lower error than expected in iteration ",i)
            return estimate
        
    
    #Returning when maxIteration exceeded
    print("Ended because max iteration count exceeded. Ended with value ",estimate)
    return estimate


# we have taken value between 0 and 0.12(diameter)
xValues=generateInputs(0,0.12,0.01)
plotGraph(xValues)
value=doBisectionMethod(0,0.12,0.5)
print(value)