import numpy as np
a=np.array([[0,1,2],[3,4,5],[6,7,8]])

print(a.ndim) # Dimension # 2
print(a.shape) # Shape #(3,3)
print(a.dtype) # Data type [by default 64bit data type is used] #int64
print(a.size) # Number of elements #9

b=np.arange(9) # 0 to 9-1 will be used to create array
print(b)
b.reshape(3,3)
print(b)


# np.zeros()
# np.ones()

def func(x):
    x+10
