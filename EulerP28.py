import time
startTime=time.clock()

size=1001
number=size**2
total=0

count=size-1

total += number
print number
while count>0:
        for i in range(4):
                number -= count
                total += number
                print number
        count -= 2
        print count

print total

endTime=time.clock()
print endTime-startTime