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
list=range(24, 28124)

while len(list):
        if len(list)%100==0:print len(list)
        x=list[0]
        #print x
        for y in range(12,x/2+1):
                if isAbun(y) and isAbun(x-y):
                        for item in list:
                                if item % x==0:
                                        finalList.append(item)
                                        list.remove(item)
                        
                        break
                        
        if x in list: list.remove(x)
# print finalList
print reduce(lambda x,y :x+y , finalList)
                        
endTime=time.clock()
print endTime-startTime