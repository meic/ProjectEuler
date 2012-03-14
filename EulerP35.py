import time
startTime=time.clock()
import primes
count=4
circPrimes=[2,3,5,7]


max=1000000
max2=100
x=4
while primes.prime(x)<max:
        numList=[int(y) for y in str(primes.prime(x))]
        contin=1
        for i in range(1,len(numList)):
                if contin:
                        newNum=0
                        for j in range(len(numList)):
                                newNum+=(10**(len(numList)-j-1))*numList[(j+i)%len(numList)]
                                # print newNum
                        # print "%i  %i" % (primes.prime(x),newNum)
                        if not primes.isprime(newNum): contin=0
        if contin:
                count +=1
                circPrimes.append(primes.prime(x))
                print circPrimes
        x +=1

print circPrimes
print count
print len(circPrimes)


endTime=time.clock()
print endTime-startTime