import matplotlib.pyplot as plt
import numpy as np

def GaussianElimination(A,B,pivot=True,showAll=False):
    # print("Hello")
    # currentPivotRow=0
    rowNumber,colNumber=np.shape(A)
    xValues=np.zeros(rowNumber,float)


    for k in range(rowNumber-1):
        if np.fabs(A[k][k]==0 and pivot==True):
            #pivoting
            maxFirstColValue=A[i][i]
            temp=0
            for j in range(i+1,colNumber):
                #A[i][j]=A[i-1][j]
                if(abs(A[j][i])>abs(maxFirstColValue)):
                    maxFirstColValue=A[j][i]
                    print(j,">", i)
                    #Switching coeffrow
                    A[[j,i]]=A[[i,j]]
                    #Switching const row
                    B[[j,i]]=B[[i,j]]
                    
                    # print(A)
                    # print(B)
        if (abs(A[k][k] == 0) and pivot==False):
            print('Divide by zero detected! ')

        for i in range(k+1,rowNumber):
            if A[i,k]==0:
                continue
            factor=A[k,k]/A[i,k]
            for j in range(k,rowNumber):
                A[i,j]=A[k,j]-A[i,j]*factor
            B[i]=B[k]-B[i]*factor
            if(showAll==True):
                print(A)
                print(B)

    #Back Substitution
    xValues[rowNumber-1]=B[rowNumber-1]/A[rowNumber-1,rowNumber-1]
    for i in range(rowNumber-2,-1,-1):
        sum=0
        for j in range(i+1,rowNumber):
            sum+=A[i,j]*xValues[j]
        xValues[i]=(B[i]-sum)/A[i,i]
    vector = []


    for i in range (rowNumber):
        xValues[i]=format(xValues[i],'.4f')
        vector.append(xValues[i])

    answer = np.array(vector).reshape(rowNumber, 1)
    ans=[]
    for i in answer:
        ans.append(i[0])
        
    return ans



            
def function(x,consts):
    val=0
    for i in range(len(consts)):
        val+=consts[i]*(x**i)
    return val
        
def polynomialRegression(xVal,yVal,order):
    xArr=np.array(xVal)
    yArr=np.array(yVal)
    length=len(xVal)

    sumX=sum(xArr)
    
    sumY=sum(yArr)
    sumXY=sum(xArr*yArr)
    sumX2=sum(xArr*xArr)

    #   Creating the coeffMatrix and the constMatrix
    coeffMatrix=np.zeros((order+1,order+1))
    constMatrix=np.zeros((order+1,1))
    #   Determining the coeffMatrix
    for i in range(order+1):
        for j in range(order+1):
            coeffMatrix[i][j]=sum(xArr**(i+j))
    #print(coeffMatrix)
    
    #   Determining the constMatrix
    for i in  range(order+1):
        constMatrix[i][0]=sum(yArr*(xArr**(i)))
    #print(constMatrix)
    
    constants=GaussianElimination(coeffMatrix,constMatrix)
    print(constants)
    return constants

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
consts=polynomialRegression(xValues,yValues,10)
xOut=sorted(xValues)
yOut=[]
for i in xOut:
    yOut.append(function(i,consts))

plt.scatter(xValues,yValues,marker="x",color="orange")
plt.plot(xOut,yOut)

# plt.xticks("")
# plt.yticks("")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.show()