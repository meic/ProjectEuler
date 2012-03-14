import time
import primes
startTime=time.clock()

NO_NEEDED=4
def isPrimeJoin(x,y):
        return (primes.isprime(x*10**(len(str(y)))+y) and primes.isprime(y*10**(len(str(x)))+x))

def nextPrime(lastPrimeIndex,depth,prime):
        for i in range(lastPrimeIndex-1,depth-1,-1):
                prime[NO_NEEDED-1-depth]=primes.prime(i)
                if depth==1:
                        yield prime
                else:
                        yield nextPrime(i, depth-1,prime)


                
def run():
        a=10
        noNeeded=4
        prime=[0 for x in range(noNeeded)]
        # while True:
                # pass
        
        for p in nextPrime(6,NO_NEEDED-1,prime):
                print p
        
        # for i,pi in nextPrime(6,3):
                # prime[0]=pi
                # for j,pj in nextPrime(i,2):
                        # prime[1]=pj
                        # for k,pk in nextPrime(j,1):
                                # prime[2]=pk
                                # for l,pl in nextPrime(k,0):
                                        # prime[3]=pl
                                        # print prime
        
        
        
        
run()



endTime=time.clock()
print endTime-startTime