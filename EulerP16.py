import time
startTime=time.clock()


number=1000
#print 2**number

strNo=str(2**number)
#print strNo
sum=0
for x in range(len(strNo)):
        sum+=int(strNo[x])

print sum

endTime=time.clock()
print endTime-startTime