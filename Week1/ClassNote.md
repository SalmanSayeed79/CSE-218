# Intro to python

- Invented by Guido van Rossum
- Current version (at the time) is 3.10.0
- 2.x versions are now obsolete
- At the time python is 3rd most popular after JS and HTML/CSS

Popular usage : 
- Data visualization
    - Matplotlib
- ML
    - pyTorch
    - TensorFlow
- Web Development
    - Django
    - Flask
- Web Scraping
    - bs4

We can download python [here](https://www.python.org/)

### Installation
---
1. We download it
2. We download our IDE for choice
3. Run our code

### Basic Programming
---
#### Data types
1. Boolean
    - bool
2. Numerical
    - float [No double]
    - int
3. Text
    - str
4. Sequence
    - list 
    - tuple
5. Mapping
    - dict

** No character type data

** No double type data


**Printing in python**
- python always prints in newline
- We can also print values without newline by putting arguement end=""
```python
#printing without newline
print("hello",end="")
print("world")
```
- Whiie printing multiple values in one print, default seperator is " "(space)
- We can change seperator by using sep=","
```python
print (1,2,3) # Default seperator would be " "
print(1,2,3,sep=",") #sep is the seperator
```
- Printing with types is also possible using "Formatted string" these are called "f-string"
```python
#formatted string
x=1
print(f"hello {x}")
```

**Type Casting**
- While integer typecasting we can specify the base to which we want to convert
```python
#Typecating values to string
a=2
newString="Hello "+str(2)
print(newString)

#casting to int
a="10"
b=int(a)
c=int(a,2) # This will treat the number as base 2 and a will then be 2
print(a,type(a))
print(b,type(b))
print(c,type(c))

#casting to binary
a="3"
b=bin(a)
print(a,type(a))
print(b,type(b))

#casting to float
a="3.5"
b=float(a)
print(a,type(a))
print(b,type(b))
```
**Variables Program**
- We don't need to mention the data type of each variable. Python intelligently typecasts each value
```python 
#int
a=1
#float 
b=2
#String
c="Hello"
d='Hello Again'
#boolean
e=true
```
- type(var) will return the type of the "var" variable
```python
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
```

- We can assign any value to any variable. Python will then change the type of that variable
```python
    a=5
    a="new" #a was int but we put a string it it. Now a will become a string type variable
```

**Boolean in python**
- Booleans are not 0 and 1 rather they are true and false
- Conditions will only accept boolean values 
```python
a=1
if(a){ # Invalid condition
    print("hello") 
}
```


### Lists in python
---

- Basic defition of lists would look something like this : 
```python
aList=[1,2,3]
print(aList) # This would print the list
```
- We can get the length of a list by the function len(array_name)
```python
#getting length
length=len(aList)
print(len)
```
- Accessing elements in python works like all other languages. We can even do negative indexing
```python
#Accessing certain element
print(aList[0])

#normal last element accessing
length=len(aList)
print(aList[length-1])

#negative indexing
print(aList[-1]) #Would print the last element
```
**Creating sub-lists**
- We can create sub-list using indexing
- The original list remains unchanged
```python
#Creating a sublist
L=[5,6,7,8,9]
#Suppose we want [6,7,8]
L2=L[1:4]
print(L2) #second one would be the element before which we'll take

#Starting from first
print(L[:3])

#Going to last 
print(L[1:])

#No first and last would give the whole array
print(L[:])

#Removing first and last element
print(L[1:-1])

#Jumping from values
print(L[::2]) #will jump 2 values [5,7,9]
``` 
**Adding values to a list**
```python
#Appending a list
L=[5,6,7,8,9]
L.append(12)# Adds 12 to the last
```
**Lists are mutable**
```python
L=[5,6,7,8,9]
L[0]=1000
print(L) #This is possible
```
**Reversing a list**
```python
#Reversing a list
L=[5,6,7,8,9]
print(L[::-1]) #Starts from last and decrements by one
```
**Lists are mutable**
```python
L=[5,6,7,8,9]
L[0]=1000
print(L) #This is possible
```

**We can add lists**

```python
L=[1,2,3]
M=[4,5,6]
N=L+M # This is valid [1,2,3,4,5,6]
O=L[1:]+M[:2] # This is also valid 
```
### Strings in python
---
- String doesn't work works like a list of characters
- We can slice a string the same way we sliced a list
```python
S="hello"
print(S)
print(S[:-1]) #This is possible because we are basically creating a substirng and the main string is unchanged

S2=["h","e","l","l","o"] #Not a string
```
- Strings are also immutable
```python
S="hello"
S[0]="A" #This will give us error
```
- Append is also not permitted but we can add strings 
```python
#Adding two strings 
S="Hello "
P="World"
Q=S+P # This is allowed
# This is possible because S and P are not changed. We're just creating a new variable
```


### Tuples in Python
---
- These are like lists but they are immutable
- We can't extend tuples too
```python
#Creating a tuple
T=(1,2,3,4,5,6)
print(T)

#Accessing remains same as lists
print(T[4])
print(T[1:3])
```

**Tuples are not mutable**
```python
L=(5,6,7,8,9)
L[0]=1000
print(L) #This is not possible
```


### Python and referral
---
- Python variables can hold any type of value. They are references to different values
```python
S="Hello" # Hello is an object and S is its ref
W=" World"

S=S+W # value of S and W are added and a new object is created. Now S will refer to that object
#"Hello" is still in memory but we can't access it anymore

S=1 #Now S will refer to an integer 1 and its type will also become 1
```

### Conditionals in Python
---
**Basic structure**
```python
v=10
if(v%2==0):
    print("Even number")
else:    
    print("ODD number")
```
**Multiple conditons**
```python
a=10
# AND
if v%2==0 and a%5==0:
    print("Divisible by 5 and 2")
else : 
    print("Not ivisible by 5 and 2")
#OR
if v%2==0 or a%5==0:
    print("Divisible by 5 and 2")
else : 
    print("Not ivisible by 5 and 2")
```

**Nested conditionals**
```python
v=10
if(v%2==0):
    print("Even number")
    print("Level 1")
    if v%5==0 :
        print("Even + Divisible by 5")
        print("Level 2")
        if v%10:
            print("Even + Divisible by 5 + Divisible by 10")
            print("Level 3")
        else : 
            print("Even + Divisible by 5 but not divisible by 5")
            print("Level 3")
    else:
        print("Even but not divisible by 5")
        print("Level 2")
else:    
    print("ODD number")
    print("Level 1")
```

### Looping in Python
**For loops**
```python
#print 1 to 100

for i in range(1,101): #goes from first arg to the one before second arg
    print(i) #prints 1 to 100
```
**Nested for loop**
```python
#nested loop
for i in range(1,4): 
    for j in range(1,3):
        print(i,j)
```

**Python checks the indentation at first and then it checks for everything else**
So an indnetation error at line 789 would mean no other line will be printed
