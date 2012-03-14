import time
import primes
startTime=time.clock()

NUM=4



def numOfUniq(mylist):
        d = {}
        for x in mylist:
            d[x] = 1
        mylist = list(d.keys())
        return len(mylist)

factors=[]
contin=1
n=2


while contin:
        count =0
        for i in range(0,NUM):
                factors=primes.factors(n+i)
                if numOfUniq(factors)<NUM:
                        break
                else:
                        count+=1
        if count==NUM:
                print n
                break
        n+=1
        

endTime=time.clock()
print endTime-startTime