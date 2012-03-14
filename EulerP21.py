import time
startTime=time.clock()
import primes
max=10000

list=[i for i in range(3,10000)]
print list[0]
finalList=[]

def findPair(n):
        sum=0
        for x in primes.all_factors(n):sum +=x
        sum -= n
        return sum
        
#print findPair(3)
x=3
y=findPair(x)
z=0
while len(list):
        print x
        if x==0: x=list[0]
        if list.count(y) != 0:
                z=findPair(y)
                if z==x:
                        if list.count(x) !=0:
                                list.remove(x)
                        #print y
                        if list.count(y) !=0:
                                list.remove(y)
                        finalList.append(x)
                        finalList.append(y)
                        x=list[0]
                        y=findPair(x)
                else:
                        if list.count(x) !=0:
                                list.remove(x)
                        x=y
                        y=z
        else:
                if list.count(x) !=0:
                        list.remove(x)
                x=y
                y=z

print finalList
print reduce(lambda x,y :x+y , finalList)
                        
endTime=time.clock()
print endTime-startTime