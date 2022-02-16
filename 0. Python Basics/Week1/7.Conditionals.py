#Nested Conditions
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



## Multiple condtions 
a=10
if v%2==0 and a%5==0:
    print("Divisible by 5 and 2")
else : 
    print("Not ivisible by 5 and 2")