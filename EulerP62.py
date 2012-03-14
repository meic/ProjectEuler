import time
startTime=time.clock()

NEEDED=5

def isPerm(int1, int2):
        str1 = str(int1)
        str2 = str(int2)
        if len(str1) != len(str2):
                return False
        for ch in str1:
                if str1.count(ch) != str2.count(ch):
                        return False
        return True

def findNext(num,max,count):
        if count==0:
                print max+1
                print (max+1)**3
                return True
                

        for n in xrange(max,0,-1):
                if isPerm(num**3,n**3):
                        if findNext(num, n-1 , count-1): return True
                        else: return False
        return False
        
def run():        
        n=10
        while True:
                print n
                if findNext(n,n-1,NEEDED-1): return 0
                
                
                n+=1


        
        
run()



endTime=time.clock()
print endTime-startTime