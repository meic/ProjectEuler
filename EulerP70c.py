import primes

def isPerm(x,y):
        x = str(x)
        y = str(y)
        if len(x)!=len(y):
                return False
        for ch in x:
                if x.count(ch)!=y.count(ch):
                        return False
        return True

maxim = 10**7      
minNOverPhy = 10**9


x=2
while primes.prime(x)<maxim:
        for y in range(1,x):
                if primes.prime(y)*primes.prime(x) > maxim:
                        break
                nOverPhy = float(primes.prime(x)*primes.prime(y))/float((primes.prime(x)-1)*(primes.prime(y) -1))
                if minNOverPhy > nOverPhy:
                        if isPerm(primes.prime(y)*primes.prime(x),(primes.prime(x)-1)*(primes.prime(y) -1) ):
                                minNOverPhy = nOverPhy
                                print primes.prime(y)*primes.prime(x), nOverPhy
                        
                        
        x+=1
        

