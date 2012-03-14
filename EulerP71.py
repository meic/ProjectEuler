import math

maxD = 10**6
minim = 0
corroD = 0
corroN = 0


target = 3./7.

for d in range(2,maxD+1):
        num = int(d*target)
        
        if 7*num == 3 *d:
                continue
        
        if float(num)/float(d) > minim:
                minim = float(num)/float(d)
                corroD = d
                corroN = num

print minim, corroN, corroD
        
        

