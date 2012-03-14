import math

Tollerance = 10**(-10)

def isInt(x):
        if abs(x-int(x))<Tollerance or abs(x-int(x)-1.)<Tollerance:
                return True
        return False
   
def run(sqrtN):
        
        a.append(int(sqrtN))
        # print len(a), int(sqrtN), 1./(sqrtN-a[-1]), 1./(sqrtN-a[-1])-math.sqrt(N)- int(1./(sqrtN-a[-1])-math.sqrt(N))
        
        
        if isInt(1./(sqrtN-a[-1])-math.sqrt(N)): 
                a.append(int(1./(sqrtN-a[-1])))
                return 0
        if len(a)>100:return 0
        
        return run(1./(sqrtN-a[-1]))
        
        
max=10000
count = 0
for N in range(2,max+1):  
        a=[]
        if not isInt(math.sqrt(N)):
                run(math.sqrt(N))
        print N,a, len(a)-1, count
        if len(a)>0 and len(a)%2==0:
                count+=1
print count