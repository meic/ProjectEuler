import time
import math
startTime=time.clock()

MAX=1000

trips=[]
prim=[]

for x in range(1,MAX):
        for y in range(1,x):
                z=math.sqrt(x**2+y**2)
                if z==int(z):
                        trips.append([x,y,z])
                        prim.append(x+y+z)
                        
pMax=0
countMax=0

for i in prim:
        if i<1000:
                if prim.count(i)>countMax:
                        pMax=i
                        countMax=prim.count(i)

print pMax
print countMax



endTime=time.clock()
print endTime-startTime