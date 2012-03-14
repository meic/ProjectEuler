import time
startTime=time.clock()

f = open(".\EulerP13.data","r")

numbers = []

for i in range(100):
        lineStr=f.readline()
        numbers.append(int(lineStr))

print reduce(lambda x,y:x+y, numbers)
        
endTime=time.clock()
print endTime-startTime