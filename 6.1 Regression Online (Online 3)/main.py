import matplotlib.pyplot as plt
import numpy as np
import math

#Values from the table
xValues=[0,5,10,15,20,25,30]
yValues=[1000,550,316,180,85,56,31]

# BEST FIT MODEL
#=========================================================
# After plotting the points in the graph, we can easily see that,
# The amount of drug is exponentially decreasing
# Thus the best fit model would be the exponential model
# The equation would have the form, y=a0*(e**(a1*x))
# We will need to find the constants a and b and design the model

# We can however, do this easily by transforming the exponential form to a linear form and use linear regerssion to do this easily.


def function(x,a0,a1):
    return a0*math.exp(a1*x)

def expLinearRegression(xVal,yVal):
    #Equation form would be
    #==========================
    #lny=lna0+a1*x

    xArr=np.array(xVal)
    yArr=np.array([np.log(a) for a in yVal])
    length=len(xVal)
    #Determining the summations
    sumX=sum(xArr)
    sumY=sum(yArr)
    sumXY=sum(xArr*yArr)
    sumX2=sum(xArr*xArr)


    a1=(length*sumXY-sumX*sumY)/(length*sumX2-sumX**2)
    a0=(sumY-a1*sumX)/length
    realA0=math.exp(a0)

    return realA0,a1
    
#Plotting the given points to predict what model should be used
plt.scatter(xValues,yValues,marker="x",color="red")

#Determining the constants
a0,a1=expLinearRegression(xValues,yValues)
print("The equation would have the form : ",a0,"e^(",a1,"x)")
#Determining the amount after 40 hrs
ans=a0*math.exp(40*a1)
print("Amount of drug in body after 40 hrs (mg) : ",ans)
plt.plot(40,ans,color="blue",marker="o")

#Declaring points for output graph
xOut=np.arange(0,50,1)
yOut=[]
for i in xOut:
    yOut.append(function(i,a0,a1))

#Plotting the graph
plt.plot(xOut,yOut,color="green")
plt.xlabel("Hours since drug was adminstered")
plt.ylabel("Amount of drug in body (mg)")
plt.title("Drug absorption experiment")
plt.show()
