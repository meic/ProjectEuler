import time
import primes
startTime=time.clock()

n=0
MAX=10**6
noPrimes=0
x=0

while primes.prime(x)<MAX/2:
        sum=primes.prime(x)
        n=1
        while sum<MAX:
                sum+=primes.prime(x+n)
                n+=1
                if primes.isprime(sum):
                        if n>noPrimes:
                                noPrimes=n
                                print noPrimes
                                print sum
        x+=1

endTime=time.clock()
print endTime-startTime