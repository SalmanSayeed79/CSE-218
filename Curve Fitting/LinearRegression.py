import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return

#   Reading from the file
#===============================================
xValues=[]
yValues=[]
file=open("data_a1.txt")
for line in file:
    tempLine=line.split()
    xValues.append(tempLine[0])
    yValues.append(tempLine[1])

print("Xvalues")
print("===========================")
print(xValues)
print("Yvalues")
print("===========================")
print(yValues)


#   Plotting the graph and points
#===============================================
plt.scatter(xValues,yValues,marker="x",color="orange")
plt.xticks("")
plt.yticks("")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.show()