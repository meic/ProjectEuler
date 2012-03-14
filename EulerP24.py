import time
startTime=time.clock()
import math

number = 1000000-1
# number=0
digits=[]
posDigits=range(10)
print posDigits

def div(x,y):
        d=int(x/y)
        r=x%y
        return d,r
# print number
# print math.factorial(9)
# d,r=div(number,math.factorial(9))
# print d
# print r
#print math.factorial(10)


for i in range(10):
        d,number=div(number,math.factorial(9-i))
        print d
        print number
        digits.append(posDigits[d])
        posDigits.remove(digits[-1])
        print digits

print digits

endTime=time.clock()
print endTime-startTime