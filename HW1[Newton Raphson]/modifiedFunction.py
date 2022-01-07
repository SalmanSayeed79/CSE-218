import matplotlib.pyplot as plt
import pandas as pd
def y(x):
    cube = pow(x,3)
    sqr= pow (x,2)
    return cube-3*0.06*sqr+4*0.000216*0.55
def findError(prev,new):
    numerator=abs(abs(new)-abs(prev))
    denominator=new
    return abs((numerator/denominator)*100)

def modifiedBisectionMethod(lowerBound,upperBound,error=0.5,maxIteration=20):
    fLower=y(lowerBound)
    fUpper=y(upperBound)
    
    estimate=upperBound
    oldEstimate=upperBound
    
    tableContent=[]
    tableLabels=["Count","Lower","Upper","Estimate","Error"]
    
    if(fLower*fUpper<0):
        print("Correct range chosen")
        
    #Returning if range is false
    else:
        print("Wrong range chosen")
        return
    
    for i in range(maxIteration):
        if (y(estimate)*y(lowerBound)>0):
            oldEstimate=estimate
            lowerBound=estimate 
            
        elif(y(estimate)*y(lowerBound)<0): 
            oldEstimate=estimate
            upperBound=estimate
        
        elif(y(estimate)==y(lowerBound)):
            return estimate
        
        estimate=(upperBound+lowerBound)/2
        currentError=findError(oldEstimate,estimate)
        
        #Debugging print
        # print("lower ",lowerBound," upper ",upperBound,"Estimate ",estimate)
        # print("Error  : ",currentError)
        
        #Creating table cell
        tableCell=[i,lowerBound,upperBound,estimate,currentError]
        tableContent.append(tableCell)
        
        
        #Returning if error found
        # if(currentError<=error):
        #     print("Got lower error than expected in iteration ",i)
        #     return
        
    
        #Returning when maxIteration exceeded
    fig, ax =plt.subplots(1,1)
    df=pd.DataFrame(tableContent,columns=tableLabels)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values,colLabels=df.columns,loc="center",colColours =["cyan"] * 5)
    plt.show()
    print("Ended because max iteration count exceeded. Ended with value ",estimate)
    return 
modifiedBisectionMethod(0,.12,.5,20)