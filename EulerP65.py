import time
import math
startTime=time.clock()


def retA(n):
        if n == 0: return 2
        if n%3==2: return 2*(n-2)/3 + 2
        return 1

def next(n,num,den):
        
        if n==-1: return num, den 
        return next(n-1,den,retA(n-1)*den+num)
        
def run():
        
        n = 100-1
        print sum([int(ch) for ch in str( next(n,1,retA(n))[0] )])
        
run()



endTime=time.clock()
print endTime-startTime