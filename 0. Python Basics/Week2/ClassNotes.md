# More python

## Functions
Functions is C looked something like this : 
```c
int Func(int x){
    // Do something
}
```
However in python they look different : 
```python
def Func(x):
    return x*x;

```

- Python lets us return multiple times in the same function
```python
def multipleReturn(x,y):
    return x/y, x%y

print(multipleReturn(5,2))
```
- We can also set default arguements using python
``` python

#Setting default arguements
def defaultArgs(x,y=7):
    return x*y

print(defaultArgs(6)) #42
print(defaultArgs(6,2)) #12
```
- We can use variable number of arguements
```python
#Using variable length arguements
def varLenFun(id,*var):
    print(id)
    #printing all other args
    for item in var:
        print(item)
    #Accessing certain arguement
    print("name is : ",var[0]) 
varLenFun(1,2,3,4,5,6,7)
```

**Passing values**
- Passing values can't be defined as "passed by value" or "passed by reference"
- Passing values happen as "Passed by object reference"
```python
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
```

### Generator functions

When calling a list or iterating through a list we bring the whole list in our memory. In case of bigger lists we use generator

```python
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

```



## Object Oriented Programming

- Classes can't have any private variables
- Members variables are defined inside the __ init __ method

```python
# No private elements
class Student:
    studentCount=0 #This is like a static variable
    def __init__(this,id, name):
        this.id=id
        this.name=name
        Student.studentCount+=1
    def showCount():
        print("Number of studnets : ",Student.studentCount)
    def showInfo(this):
        print("ID : ",this.id, " Name : ",this.name)
        
tripto=Student("1205001", "Nafis Irtiza")
sadat=Student("1905079", "Sadat Hossain")
sadat1=Student("1905079", "Sadat Hossain")
sadat2=Student("1905079", "Sadat Hossain")
sadat3=Student("1905079", "Sadat Hossain")
sadat4=Student("1905079", "Sadat Hossain")
sadat5=Student("1905079", "Sadat Hossain")
```
```python
# Accessing member variables using member function
sadat.showInfo()
tripto.showInfo()
```
```python
# Directly accessing values of an object because all object data is public
print(tripto.name,tripto.id)
print(sadat.name,sadat.id)
```
```python
# Accessing static variables is as simple as calling it with the variableName 
print(Student.studentCount)
```
```python
# Deleting member variables 
del tripto.name
print(tripto.name) # will show error
```
- Deleting static variables
```python
# Deleting static variables
del Student.studentCount
print(Student.studentCount) # will show error
```
## Modules

- Importing a whole library
```python
# importing a whole library
import math
print(math.ceil(5.5))
```
- importing certain element from a function
```python
#importing certain element from a function
from math import ceil
print(ceil(5.5))
```
- importing all
```python
from Modules_Export import *
```
- Seleting elements of a file for not exporting
```python
if __name__=="__main__":      
    # Things after this part will not be exported
```


## Global Variables

__Normally__
```python
a=300
def func():
    a=3 # this is local. Both the a is different
func()
print(a)
```
__Using "Global"__
```python
a=300
def func():
    global a
    a=3 # now this is the global a
func()
print(a)
```

## Console I/O

```python
print("Enter your name : ")
a=input()
print("Hello ,",a)
```

## File I/O

**Reading files**
- Reading the whole file at once
```python
with open("input.txt","r") as fileInput:
    # Reading whole document at once
    st=fileInput.read()
    print(st)
    fileInput.close()
```
- Reading line by line
```python
with open("input.txt","r") as fileInput:
    # Reading line by line
    for line in fileInput:
        print("NewLine : ",line)
    fileInput.close()
```






























