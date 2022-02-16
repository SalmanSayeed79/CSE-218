import numpy as np
import matplotlib.pyplot as plt

yvalues=np.array([1,2,3,4,5])
plt.plot(yvalues)
plt.show()

# Using both x and y values
xval=np.array([i for i in range(1,6)])
yval=np.array([i*i for i in range(1,6)])
plt.plot(xval,yval,"--",marker="o")
plt.show()

# Using multiple y-values
xval=np.array([i for i in range(1,6)])
yval1=np.array([i*i for i in range(1,6)])
yval2=np.array([i*3 for i in range(1,6)])
plt.plot(xval,yval1,yval2,"--",marker="o")
plt.show()