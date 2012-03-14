import time
startTime=time.clock()

number=5
max=10**7 

list=[]
totalSum=0


def isGood(n):
        sum=0
        for i in range(len(str(n))):
                sum += int(str(n)[i])**number
        if sum==n: return True
        return False

for i in range(2,max):
        if isGood(i):
                list.append(i)
                print list
                print reduce(lambda x,y: x+y, list)

print reduce(lambda x,y: x+y, list)
                
                
endTime=time.clock()
print endTime-startTime