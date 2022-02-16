import numpy as np
import matplotlib.pyplot as plt

mu=10 # Average
sigma=10 # Standard Deviation

x=mu+sigma*np.random.randn(10000,3) # We are taking 10000
n_bucket=100 # Each line represents a bucket. How many things per bucket is n_bucket
labels=["red","green","blue"]
plt.hist(x,n_bucket,histtype="bar",color=labels,label=labels)
plt.show()