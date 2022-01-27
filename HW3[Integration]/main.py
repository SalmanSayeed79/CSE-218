import matplotlib.pyplot as plt

def f(x):
    Cme=5*pow(10,-4)
    numerator=6.73*x+6.725*pow(10,-8)+7.26*pow(10,-4)*Cme
    denominator=3.62*pow(10,-12)*x+3.908*pow(10,-8)*x*Cme
    #print(-numerator/denominator)
    return -(numerator/denominator)


def trapezoidIntregation(start,end, intervalCount): 
    h=(end-start)/(intervalCount)
    value=f(start)+f(end)
    for i in range(1,intervalCount):
        value=value+2*f(start+h*i)
    value=value*(h/2)
    #print(value)
    return value
def simpsonsIntegration(start,end,intervalCount):
    # Making 2*intervalCount sub-intervals
    h=(end-start)/(2*intervalCount)
    value=f(start)
    for i in range(1,2*intervalCount):
        if i%2!=0:
            value+=4*f(start+i*h)
        else:
            value+=2*f(start+i*h)
    value+=f(end)
    value*=(h/3)
    return value
def getRelativeApproximateError(new,prev):
    return abs(new-prev)*100/prev

print("Trapezoid Integration : ")
print("===================================================")
first=trapezoidIntregation(1.22*pow(10,-4),0.61*pow(10,-4),1)
second=trapezoidIntregation(1.22*pow(10,-4),0.61*pow(10,-4),2)
third=trapezoidIntregation(1.22*pow(10,-4),0.61*pow(10,-4),3)
fourth=trapezoidIntregation(1.22*pow(10,-4),0.61*pow(10,-4),4)
fifth=trapezoidIntregation(1.22*pow(10,-4),0.61*pow(10,-4),5)

print("Intervals 1 : Time Taken : %20f"% first,"Absolute Relative Approx Error : ---")
print("Intervals 2 : Time Taken : %20f"% second,"Absolute Relative Approx Error : " ,getRelativeApproximateError(second,first))
print("Intervals 3 : Time Taken : %20f"% third,"Absolute Relative Approx Error : ", getRelativeApproximateError(third,second))
print("Intervals 4 : Time Taken : %20f"% fourth,"Absolute Relative Approx Error : ", getRelativeApproximateError(fourth,third))
print("Intervals 5 : Time Taken : %20f"% fifth,"Absolute Relative Approx Error : ", getRelativeApproximateError(fifth,fourth))



simpsonfirst=simpsonsIntegration(1.22*pow(10,-4),0.61*pow(10,-4),1)
simpsonsecond=simpsonsIntegration(1.22*pow(10,-4),0.61*pow(10,-4),2)
simpsonthird=simpsonsIntegration(1.22*pow(10,-4),0.61*pow(10,-4),3)
simpsonfourth=simpsonsIntegration(1.22*pow(10,-4),0.61*pow(10,-4),4)
simpsonfifth=simpsonsIntegration(1.22*pow(10,-4),0.61*pow(10,-4),5)
print("Simpsons Integration : ")
print("===================================================")
print("Intervals 1 : Time Taken : %.20f"% simpsonfirst,"Absolute Relative Approx Error : ---")
print("Intervals 2 : Time Taken : %.20f"% simpsonsecond,"Absolute Relative Approx Error : " ,getRelativeApproximateError(simpsonsecond,simpsonfirst))
print("Intervals 3 : Time Taken : %.20f"% simpsonthird,"Absolute Relative Approx Error : ", getRelativeApproximateError(simpsonthird,simpsonsecond))
print("Intervals 4 : Time Taken : %.20f"% simpsonfourth,"Absolute Relative Approx Error : ", getRelativeApproximateError(simpsonfourth,simpsonthird))
print("Intervals 5 : Time Taken : %.20f"% simpsonfifth,"Absolute Relative Approx Error : ", getRelativeApproximateError(simpsonfifth,simpsonfourth))



#=============================================
# Creating graph
#=============================================
x=[1.22*pow(10,-4),1.20*pow(10,-4),1.0*pow(10,-4),0.8*pow(10,-4),0.6*pow(10,-4),0.4*pow(10,-4),0.2*pow(10,-4)]

y=[0]
for i in range(1,len(x)):
    y.append(simpsonsIntegration(x[0],x[i],5))

x.reverse()
y.reverse()
plt.plot(x,y,marker="o")
plt.xlabel("Oxygen Concentration")
plt.ylabel("Time")
plt.grid()
plt.show()
# print(y)