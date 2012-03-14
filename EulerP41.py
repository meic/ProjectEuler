import time
import primes
startTime=time.clock()

length =7

n=7654321
contin=1

while True:
        if n%1000==0:print n
        if n<10**5:length =6
        if n<10**4:length =5
        if n<10**3:length =4
        
        contin=1
        for i in range(1,length+1):
                if str(n).count(str(i))!=1:
                        contin=0
                        break
        if contin:
                if primes.isprime(n):
                        print n
                        break
        n-=1
        
        
endTime=time.clock()
print endTime-startTime