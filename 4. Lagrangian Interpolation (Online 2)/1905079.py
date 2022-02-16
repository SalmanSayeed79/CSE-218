
import matplotlib.pyplot as plt
import numpy as np

xValues=[]
yValues=[]
def ReadFile(fileName):
    file=open(fileName,"r")
    for line in file:
        eachLineArr=line.split()
        if(eachLineArr[0] and eachLineArr[0].isnumeric()):
            xValues.append(float(eachLineArr[0]))
            yValues.append(float(eachLineArr[1]))
    file.close()



def chooseInterval(xArray, xTarget, count):
    length = len(xArray)
    dist = np.empty(length-count)
    for i in range(length-count):
        dist[i] = 0
        for j in range(count+1):
            dist[i] += np.abs(xTarget-xArray[i+j])

    minIndex = 0
    for i in range(length-count):
        if(dist[i]<dist[minIndex]):
            minIndex = i
    
    return minIndex

def lagrangianMethod(xVal,yVal,xTarget,degree):
    startIndex=chooseInterval(xVal,xTarget,degree+1)
    coeffs=np.ones(degree+1)
    for i in range(degree+1):
        for j in range(degree+1):
            if(i!=j):
                coeffs[i]=coeffs[i]*(xTarget-xVal[j])/(xVal[i]-xVal[j])
    ans=0
    for i in range(degree+1):
        ans+=coeffs[i]*yVal[i]
    return ans
    
def getError(new,prev):
    error=abs(new-prev)/abs(new) 
    return error*100
ReadFile("stock.txt")
# print(xValues)
# print(yValues)

target=float(input())

first=chooseInterval(xValues,target,2)
second=chooseInterval(xValues,target,3)
#third=chooseInterval(xValues,target,4)

quadraticApprox=lagrangianMethod(xValues[first:first+3],yValues[first:first+3],target,2)
cubicApprox=lagrangianMethod(xValues[second:second+4],yValues[second:second+4],target,3)
#quartileApprox=lagrangianMethod(xValues[third:third+5],yValues[third:third+5],target,4)
# val=[xValues,yValues]
# print(val)


#plotting the whole graph
plt.plot(xValues,yValues)
#plotting the point 
plt.plot(target,quadraticApprox,marker="o")
plt.plot(target,cubicApprox,marker="o",mec="purple",mfc="purple")
#plt.plot(target,quartileApprox,marker="o")

# print(cubicApprox)
# print(quadraticApprox)
# #print(quartileApprox)

print("Error","{:.2f}".format(getError(cubicApprox,quadraticApprox)),"%")
plt.show()