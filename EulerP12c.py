import primes
import time
startTime=time.clock()

noFactors=0
n=1
while noFactors <=500:
        tri = n*(n+1)/2
        noFactors = primes.num_factors(tri)
        #print noFactors
        n +=1
print n-1
print tri

endTime=time.clock()
print endTime-startTime