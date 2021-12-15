import numpy as np

#=========================================
# Defining the main function to implement Gaussian
#=========================================

def useGaussian(matrixParam, size):
    # Things I need to do here:
    #=========================================
    # Traverse through the matrix row by row
    # Define a pivot 
    # [Forward Elimination] Use the pivot to create a upper valued matrix
    # [Back Substitution] Then equalize each row with the correspoding const to from equations
    # Solve the equations derived by back substitution
    for i in range(size):



#=========================================
# Taking the input to create matrices 
#=========================================
equationCount=int(input())
coeffMatrix=np.array(equationCount,equationCount)
constMatrix=np.array(equationCount,1)
for i in range(equationCount):
    for j in coeffMatrix[i-1]:
        coeffMatrix[i-1][j-1]=int(input())
for i in range(equationCount):
    constMatrix[i-1][0]=int(input())

print(coeffMatrix)
print(constMatrix)