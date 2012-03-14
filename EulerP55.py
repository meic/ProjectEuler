import time
startTime=time.clock()

def revAndAdd(x):
        listx=[int(ch) for ch in str(x)]
        # listx.reverse()
        sum=0
        for i in range(len(listx)):
                sum+=listx[i]*10**i
        return sum+x

def ispal(x):
        for n in range(len(str(x))/2):
                if str(x)[n]!=str(x)[-1-n]:
                        return False
        return True

def test(x):
        count =0
        while count<=50:
                x=revAndAdd(x)
                if ispal(x): return True
                count += 1
        return False
        
def run():
        n=10
        countl=0
        while n<=10000:
                if not test(n):countl+=1
                n+=1
        
        print countl

run()



endTime=time.clock()
print endTime-startTime