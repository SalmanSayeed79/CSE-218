import numpy as np

#=========================================
# Defining the main function to implement Gaussian
#=========================================

# def useGaussian(matrixParam, size):
#     # Things I need to do here:
#     #=========================================
#     # Traverse through the matrix row by row
#     # Define a pivot 
#     # [Forward Elimination] Use the pivot to create a upper valued matrix
#     # [Back Substitution] Then equalize each row with the correspoding const to from equations
#     # Solve the equations derived by back substitution
#     for i in range(size):


def GaussianElimination(A,B,pivot=False,showAll=True):
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
    return answer


def GaussianElimination2(A,B,pivot=True,showAll=False):
    rowNumber,colNumber=np.shape(A)
    for i in range(rowNumber):
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
                
        #Forward Elimination
        
        for j in range(i,colNumber-1):
            factor=A[i,i]/A[i+1,i]
            print(A[i,i],"/",A[i+1,i])
            

#=========================================
# Taking the input to create matrices 
#=========================================


equationCount=int(input())
coeffMatrix=np.zeros((equationCount,equationCount))
constMatrix=np.zeros((equationCount,1))

for i in range(equationCount):
    inputLine=input()
    inputLine=inputLine.split()
    
    for j in range(equationCount):
        coeffMatrix[i][j]=float(inputLine[j])
for i in range(equationCount):
    constMatrix[i][0]=float(input())

print(coeffMatrix)
print(constMatrix)

GaussianElimination2(coeffMatrix,constMatrix,True,True)
# answer=GaussianElimination(coeffMatrix,constMatrix,True,True)
# print(answer)