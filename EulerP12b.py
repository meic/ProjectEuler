import sys


primes=[2,3]

def findNextPrime():
        n=primes[-1]+1
        while True:
                if isPrime(n): return n
                n+=1
                
def isPrime(n):
        for p in primes:
                if n % p == 0:
                        return False
        return True

        
#while primes[-1]<20:
#        primes.append(findNextPrime())
        
#print primes
dic={}
n=2
count=0
countMax=0
while count<=500:
        tri = n*(n+1)/2
        #print tri
        count=0
        found=False
        x=tri
        dic.clear()
        while x>1:
                found=False
                for p in primes:
                        if x%p==0:
                                x=x/p
                                #print x
                                if dic.has_key(p):
                                        dic[p]+=1
                                else:
                                        dic[p]=1
                                
                                found=True
                if found==False and x>1:
                        primes.append(findNextPrime())
        #print dic.values()
        count = reduce(lambda x,y:x*y , dic.values())
        if count>countMax:
                countMax=count
                print countMax
                print n
        n+=1
print n-1
print tri