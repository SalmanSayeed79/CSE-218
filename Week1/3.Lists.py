aList=[1,2,3]
# We can even print the list
print(aList)
#Accessing certain element
print(aList[0])

#negative element
print(aList[-2]) #Would print the last element

#getting length
len=len(aList)
print(len)

#Creating a sublist
L=[5,6,7,8,9]
#Suppose we want [6,7,8]
print(L[1:4]) #second one would be the element before which we'll take

#Starting from first
print(L[:3])

#Going to last 
print(L[1:])

#No first and last would give the whole array
print(L[:])

#Removing first and last element
print(L[1:-1])

#Jumping from values
print(L[::2]) #will jump 2 values

#Reversing a list
L=[5,6,7,8,9]
print(L[::-1]) #Starts from last and decrements by one


#==================================
# Mutability
#==================================

L[0]=1000
print(L)