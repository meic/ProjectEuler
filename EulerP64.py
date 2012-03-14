import time
import math
startTime=time.clock()

NEEDED=5
TOLLERANCE = 10**-5
def next(count,n,alpha,beta,gamma):
        if gamma == 0: return 0
        x=(float(alpha)*math.sqrt(n)+float(beta))/float(gamma)
        a=int(x)
        
        #print float(beta)/gamma,beta/gamma,float(beta)/gamma-beta/gamma
        if count>0 and (alpha/gamma==1) and ((float(beta)/gamma-beta/gamma)<TOLLERANCE):
                return count
        return next(count+1,n,alpha*gamma, -gamma*(beta-gamma*a), (alpha**2)*n-(beta-gamma*a)**2)

        
def run():    
        count=0
        for n in range(2,10001):
                
                print n, next(0,n,1,0,1), next(0,n,1,0,1) % 2 == 1
                if next(0,n,1,0,1) % 2 == 1: count += 1
        print count

        
        
run()



endTime=time.clock()
print endTime-startTime