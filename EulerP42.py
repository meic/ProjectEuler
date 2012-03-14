import time
import math
startTime=time.clock()

f = open(".\EulerP42.data","r")

line=f.readline()
list=line.split(",")

count=0
tris=[]

def isTri(x):
        if x in tris:
                return True
        n=(math.sqrt(1+8*x)-1)/2.0
        if n==int(n):
                tris.append(x)
                return True
        return False


for word in list:
        sum=0
        for ch in word[1:-1]:
                sum+=ord(ch)-64
        if isTri(sum):
                count+=1

print count
        


endTime=time.clock()
print endTime-startTime