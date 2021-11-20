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
def func():
    print("From another file!")
if __name__=="__main__":        
    tripto=Student("1205001", "Nafis Irtiza")
    sadat=Student("1905079", "Sadat Hossain")
    sadat1=Student("1905079", "Sadat Hossain")
    sadat2=Student("1905079", "Sadat Hossain")
    sadat3=Student("1905079", "Sadat Hossain")
    sadat4=Student("1905079", "Sadat Hossain")
    sadat5=Student("1905079", "Sadat Hossain")

