#Basic function
def func(x):
    print("Hello ",x)

#Multiple returns from a single function
def multipleReturn(x,y):
    return x/y, x%y

print(multipleReturn(5,2))

#Setting default arguements
def defaultArgs(x,y=7):
    return x*y

print(defaultArgs(6)) #42
print(defaultArgs(6,2)) #12

#Using variable length arguements
def varLenFun(id,*var):
    print(id)
    #printing all other args
    for item in var:
        print(item)
    #Accessing certain arguement
    print("name is : ",var[0]) 
varLenFun(1,2,3,4,5,6,7)

#Passing values
    # Passing values can't be defined as "passed by value" or "passed by reference"
    # Passing values happen as "Passed by object reference"
def reAssign(lst): #A new ref gets created
    lst=[0,1]
    #This lst would get out of scope when the function ends
def append(lst):
    lst.append(3)
lst=[0]

reAssign(lst)
print("after reassignment : ",lst)
append(lst)
print("After appending : ",lst)

#Generator
    # When calling a list or iterating through a list we bring the whole list in our memory. In case of bigger lists we use generator
def GeneratorFunction():
    i=0
    for j in range(10000):
        yield i #We use this instead of return. When a normal function runs, the function ends but yield does not
        i+=1
        print("Calling",i)
        
#We have to create objects out of generators and use next to iterate through it
obj=GeneratorFunction()
for i in range(1000):
    print(next(obj)) #next helps get the next yield

















