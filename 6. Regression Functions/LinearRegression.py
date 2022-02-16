import matplotlib.pyplot as plt
import numpy as np

def function(x,a0,a1):
    return a0+a1*x
def linearRegression(xVal,yVal):
    xArr=np.array(xVal)
    yArr=np.array(yVal)
    length=len(xVal)

    sumX=sum(xArr)
    sumY=sum(yArr)
    sumXY=sum(xArr*yArr)
    sumX2=sum(xArr*xArr)

    a1=(length*sumXY-sumX*sumY)/(length*sumX2-sumX**2)
    a0=(sumY-a1*sumX)/length
    
    return a0,a1


#   Reading from the file
#===============================================
xValues=[]
yValues=[]

file=open("data_a1.txt")
for line in file:
    tempLine=line.split()
    xValues.append(float(tempLine[0]))
    yValues.append(float(tempLine[1]))



#   Plotting the graph and points
#===============================================
a0,a1=linearRegression(xValues,yValues)
xOut=np.arange(0,2,0.25)
yOut=[]
for i in xOut:
    yOut.append(function(i,a0,a1))
    
plt.scatter(xValues,yValues,marker="x",color="orange")
plt.plot(xOut,yOut)
# plt.xticks("")
# plt.yticks("")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.show()