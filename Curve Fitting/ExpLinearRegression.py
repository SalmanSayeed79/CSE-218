import matplotlib.pyplot as plt
import numpy as np
import math

def function(x,a0,a1):
    return a0*math.exp(a1*x)

def expLinearRegression(xVal,yVal):
    #Equation form would be
    #==========================
    #   lny=lna+bx

    xArr=np.array(xVal)
    yArr=np.array([np.log(a) for a in yVal])
    length=len(xVal)
    #   Determining the summations
    sumX=sum(xArr)
    sumY=sum(yArr)
    sumXY=sum(xArr*yArr)
    sumX2=sum(xArr*xArr)


    a1=(length*sumXY-sumX*sumY)/(length*sumX2-sumX**2)
    a0=(sumY-a1*sumX)/length
    realA0=math.exp(a0)

    return realA0,a1
    

#   Reading from the file
#===============================================
xValues=[0,0.01,0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19,0.21]
yValues=[1,1.03,1.06,1.38,2.09,3.54,6.41,12.6,22.1,39.05,65.32,99.78]

# file=open("data_a1.txt")
# for line in file:
#     tempLine=line.split()
#     xValues.append(float(tempLine[0]))
#     yValues.append(float(tempLine[1]))



#   Plotting the graph and points
#===============================================

a0,a1=expLinearRegression(xValues,yValues)
xOut=np.arange(-0.2,0.25,0.001)
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