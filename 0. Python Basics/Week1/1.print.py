print("Hello world")
print (1,2,3)
print(1,2,3,sep=",") #sep is the seperator
#printing without newline
print("hello",end="")
print("world")
#formatted string
x=1
print(f"hello {x}")

a=2
newString="Hello "+str(a)
print(newString)

#casting to int
a="10"
b=int(a)
c=int(a,2)
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