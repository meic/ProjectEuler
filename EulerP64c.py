from math import sqrt
 

 
def run(N):
        odd_period = 0
        L = 10000

        r = limit = int(sqrt(N))
        if limit*limit == N: return 0
        k, period = 1, 0
        while period<100:
                k = (N - r * r) / k
                r = ((limit + r) / k) * k - r
                print r
                period += 1
        if period % 2 == 1: odd_period += 1
 
run(2)
 
# print "Answer to PE64 =", odd_period