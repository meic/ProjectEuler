import time
startTime=time.clock()

import math
totalSum=0

x=3
while True:
        xList=[int(n) for n in str(x)]
        sum=0
        for n in xList:
                sum += math.factorial(n)
        
        if sum==x:
                totalSum += sum
                print x
                print totalSum
        x+=1
        
endTime=time.clock()
print endTime-startTime