import time
import math
startTime=time.clock()

pents=[]
def ispent(x):
        if pents.count(x):
                return True
        num=(1+math.sqrt(1+24.0*x))/6.0
        if num==int(num):
                pents.append(x)
                return True
        return False
        
tris=[]
def istri(x):
        if tris.count(x):
                return True
        num=(-1+math.sqrt(1+8.0*x))/2.0
        if num==int(num):
                tris.append(x)
                return True
        return False
        
def hex(x):
        return x*(2*x-1)
        
n=140
        
while True:
        if ispent(hex(n)) and istri(hex(n)):
                print n
                print hex(n)
        n+=1
        
endTime=time.clock()
print endTime-startTime