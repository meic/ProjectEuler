import time
import primes
import math
startTime=time.clock()

def check(n):
        if primes.isprime(n): return (n+2)
        
        x=0
        while primes.prime(x)<n:
                square=math.sqrt((n-primes.prime(x))/2.0)
                if square==int(square):
                        return (n+2)
                x+=1
        print n
        
num=3
while num:
        print num
        num=check(num)

endTime=time.clock()
print endTime-startTime