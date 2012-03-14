import time
import math
startTime=time.clock()

n=10**18
k=10**9

num=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print num%7

endTime=time.clock()
print endTime-startTime