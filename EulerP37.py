import time
startTime=time.clock()

import primes
n=4
count=0
sum =0
tprimes=[]

while count < 1000000000000000:
        primeList=[int(x) for x in str(primes.prime(n))]
        good=1
        for x in range(1,len(primeList)):
                primeL=0
                primeR=0
                
                for i in range(len(primeList)-x):
                        # print primeList
                        primeL+=(10**(len(primeList)-x-i-1))*primeList[x+i]
                        primeR+=(10**(len(primeList)-x-i-1))*primeList[i]
                        # print primeR
                if not (primes.isprime(primeL) and primes.isprime(primeR)):
                        good=0
                        break
        if good:
                tprimes.append(primes.prime(n))
                count +=1
                sum += primes.prime(n)
                print tprimes
                print sum
        
        n+=1
print tprimes
print sum
endTime=time.clock()
print endTime-startTime