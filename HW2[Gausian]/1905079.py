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
    rowNumber=A.shape[0]
    xValues=np.zeros(rowNumber,float)
    
    
    # for i in range(rowNumber):
    #     shapeInsideRow=A[i].shape[0]
        
    #     #pivoting
    #     maxFirstColValue=A[i][i]
    #     for j in range(shapeInsideRow):
    #         #A[i][j]=A[i-1][j]
    #         if(A[j][i]>maxFirstColValue):
    #             print(j,"matches with ", i)
    #             #Switching coeffrow
    #             A[[j,i]]=A[[i,j]]
    #             #Switching const row
    #             temp=B[j]
    #             B[j]=B[i]
    #             B[i]=temp
                
    #             print(A)
    #             print(B)
    #     #Forward Elimination
    #     for j in range(shapeInsideRow-1):
    #         #factor=A[i+1,j]/A[i,j]
    #         print(A[i,j+1],"/",A[i,j]) 

    for k in range(rowNumber-1):
        if np.fabs(A[k][k]==0 and pivot==True):
            max = A[k, k]
            for i in range(k+1,rowNumber):

                if np.fabs(A[i,k]>np.fabs(max)):
                    max=A[i,k]
                    max_val=i


            A[[k,max_val]]=A[[max_val,k]]
            B[[k,max_val]]=B[[max_val,k]]

        if np.fabs(A[k][k] == 0 and pivot==False):
            print('Divide by zero detected! Please set pivoting flag as True.')

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

answer=GaussianElimination(coeffMatrix,constMatrix,True,True)
print(answer)