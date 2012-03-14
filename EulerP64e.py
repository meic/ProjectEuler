import math, itertools

def cf_period(r):
        p = int(math.sqrt(r))   # floor of sqrt(r)
        if p*p == r: return 0   # Square number
        q=1
        remainders = {}
        a=[]
        for pos in itertools.count(1):
                q=(r-(p*p))/q
                floor=int((math.sqrt(r)+p) /float(q))
                # a.append(floor)
                p = -1* (p- (floor*q))
                if (p,q) in remainders:
                        # print r, a, pos-remainders[p,q]
                        return pos-remainders[p,q]
        remainders[p,q] = pos

print len([x for x in range(2,14) if cf_period(x)%2==1])