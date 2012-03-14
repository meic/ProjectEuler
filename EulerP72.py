import primes


def phy(x):
        d={}
        for factor in primes.factors(x):
                d[factor]=0
        
        
        num = reduce(lambda x,y:x*y , [z-1 for z in d])
        den = reduce(lambda x,y:x*y , [z for z in d])
        
        return (x*num)/den

maxim = 10**6      

sum=0  
for i in range(2,maxim+1):
        if i % 10**5 == 0: print str(i/ 10**5,) + '%'
        sum+= phy(i)
        
print sum

