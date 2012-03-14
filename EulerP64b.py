import time
import math
startTime=time.clock()

NEEDED=5
TOLLERANCE = 10**-5
def next(count,n,x,a):
        
        
        if count>0 and (x**2-n)-int(x**2-n) < TOLLERANCE:
                return count
        
        a_1=int(x)
        x_1=1/(x-a)
        return next(count+1,n,x_1,a_1)

        
def run():    
        count=0
        #for n in range(2,10001):
        for n in range(2,14):
                #print int(math.sqrt(n)),math.sqrt(n),int(math.sqrt(n))-math.sqrt(n)
                if abs(int(math.sqrt(n))-math.sqrt(n))>TOLLERANCE:
                        print n, next(0,n,math.sqrt(n),int(math.sqrt(n)))-1, (next(0,n,math.sqrt(n),int(math.sqrt(n)))-1) % 2 == 1
                        if (next(0,n,math.sqrt(n),int(math.sqrt(n)))-1) % 2 == 1: count += 1
        print count

        
        
run()



endTime=time.clock()
print endTime-startTime