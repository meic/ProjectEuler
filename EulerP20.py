import time
startTime=time.clock()

import math

number=math.factorial(100)
#print 2**number

strNo=str(number)
#print strNo
sum=0
for x in range(len(strNo)):
        sum+=int(strNo[x])

print sum

endTime=time.clock()
print endTime-startTime