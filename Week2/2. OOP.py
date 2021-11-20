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

# Accessing member variables using member function
sadat.showInfo()
tripto.showInfo()

# Directly accessing values of an object because all object data is public
print(tripto.name,tripto.id)
print(sadat.name,sadat.id)

# Accessing static variables is as simple as calling it with the variableName 
print(Student.studentCount)

# Deleting member variables 
del tripto.name
print(tripto.name) # will show error

# Deleting static variables
del Student.studentCount
print(Student.studentCount) # will show error

