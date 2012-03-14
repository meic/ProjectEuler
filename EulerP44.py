import time
import math
startTime=time.clock()

pents=[]
def ispent(x):
        if pents.count(x):
                return True
        num=(1+math.sqrt(1+24.0*x))/6.0
        if num==int(num):
                pents.append(x)
                return True
        return False
        
def pent(x):
        return x*(3*x-1)/2
        
dMin=100000000000000000000000000000000000000000000000000

for i in range(1,100000):
        if i%1000==0:print i/1000
        for j in range(1,i):
                if ispent(pent(i)+pent(j)):
                        if ispent(pent(i)-pent(j)):
                                if (pent(i)-pent(j))<dMin:
                                        dMin=pent(i)-pent(j)
                                        print dMin
                                        print i
                                        print j
                                
        
        
endTime=time.clock()
print endTime-startTime