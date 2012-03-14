import primes


def phy(x):
        d={}
        for factor in primes.factors(x):
                d[factor]=0
        
        
        num = reduce(lambda x,y:x*y , [z-1 for z in d])
        den = reduce(lambda x,y:x*y , [z for z in d])
        
        return (x*num)/den

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
  
for i in range(maxim,1,-1):
        nOverPhy = float(i)/float(phy(i))
        if minNOverPhy > nOverPhy:
                if isPerm(i, phy(i)):
                        minNOverPhy = nOverPhy
                        print i, nOverPhy
        

