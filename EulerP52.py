import time
import permute
startTime=time.clock()
        
x=1

contin=1
while contin:
        num=[int(ch) for ch in str(x)]
        if x%1000==0:print x
        good=1
        for n in range(2,7):
        
                num2=[int(ch) for ch in str(n*x)]
                
                if len(num)==len(num2) and good:
                        for i in num:
                                if num.count(i)!=num2.count(i):
                                        good=0
                                        break
                else:
                        good=0
        if good:
                contin=0
                print x
        x+=1

endTime=time.clock()
print endTime-startTime