import numpy as np
def f(x,y){
    sqr1=x**2
    sqr2=y**2

    return 
}

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