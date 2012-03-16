import math
import Euler

maxL = 1500000

count = [0,]*maxL

for m in range(2,int(math.sqrt( maxL ))+1):
        for n in range(1,m):
                #primary length = 2m(m+n)
                
                #need to check if primative
                if Euler.gcd(2*m*n,m**2 - n**2)==1:
                
                        L= 2*m*(m+n)
                        if L<=maxL:
                                for s in range(L,maxL,L): #summ over multiples of the primary length
                                        # if k*L > len(count)-1: print k, L, k*L
                                        count[s-1]+=1
                        else: 
                                continue
print count.count(1)