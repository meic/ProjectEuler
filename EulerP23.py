import time
startTime=time.clock()
import primes
max=10000

list=[i for i in range(3,10000)]
#print list[0]
finalList=[]

def factorSum(n):
        sum=0
        for x in primes.all_factors(n):sum +=x
        sum -= n
        return sum

abuns=[]        
        
def isAbun(n):
        if n in abuns: return True
        if factorSum(n)>n:
                abuns.append(n)
                return True
        return False

finalList=[]
        
for x in range(24, 28124):
        if x %100 == 0: print x
        for y in range(12,x/2+1):
                if isAbun(y) and isAbun(x-y):
                        finalList.append(x)
                        break
# print finalList
print reduce(lambda x,y :x+y , finalList)
                        
endTime=time.clock()
print endTime-startTime