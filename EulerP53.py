import time
import math
startTime=time.clock()
        
def combin(n,r):
        return (math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
     
def run():     
        count=0
        for n in range(23,101):
                for r in range(1,n):
                        if combin(n,r)>10**6:
                                count+=1
        print count
        
run()

endTime=time.clock()
print endTime-startTime