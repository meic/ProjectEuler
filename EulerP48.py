import time
startTime=time.clock()

sum=0
for n in range(1,1001):
        sum+=n**n

print sum

endTime=time.clock()
print endTime-startTime