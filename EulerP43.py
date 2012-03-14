import time
startTime=time.clock()

from permute import permList
import math

oneper=int(math.factorial(10)/100)
# print oneper
numbers=[]
checks=[2,3,5,7,11,13,17]
n=1

for i in permList(range(9,-1,-1)):
        if n%oneper==0:
                print n/oneper
                # print i
        good=1
        for j in range(7):
                if ((i[j+1]*100+i[j+2]*10+i[j+3])%checks[j]):
                        good=0
                        break
        if good:
                print i
                sum=0
                for j in range(10):
                        sum+=i[-1-j]*10**j
                print sum
                numbers.append(sum)
        n+=1

print reduce(lambda x,y:x+y, numbers)
        
endTime=time.clock()
print endTime-startTime