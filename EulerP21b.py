import time
startTime=time.clock()
import primes
max=10000

list=[i for i in range(3,10000)]
#print list[0]
finalList=[]

def findPair(n):
        sum=0
        for x in primes.all_factors(n):sum +=x
        sum -= n
        return sum
        
x=1
y=1
z=1

        
while len(list)!=0:
        
        x=list[0]
        if x % 100 == 0: print x
        y=findPair(x)
        
        if findPair(y)==x and x!=y:
                finalList.append(x)
                finalList.append(y)
                list.remove(x)
                list.remove(y)
                
        else:
                list.remove(x)
        

print finalList
print reduce(lambda x,y :x+y , finalList)
                        
endTime=time.clock()
print endTime-startTime