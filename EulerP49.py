import time
import permute
import primes
startTime=time.clock()

oneper=(9997-1000)/100

for i in range(1000,9997):
        if i%oneper==0:print i/oneper
        for j in range(1,(9999-i)/2+1):
                if primes.isprime(i) and primes.isprime(i+j) and primes.isprime(i+2*j):
                        if permute.isPerm([int(ch) for ch in str(i)],[int(ch) for ch in str(i+j)]) and permute.isPerm([int(ch) for ch in str(i)],[int(ch) for ch in str(i+2*j)]):
                                print i
                                print i+j
                                print i+2*j
                


endTime=time.clock()
print endTime-startTime