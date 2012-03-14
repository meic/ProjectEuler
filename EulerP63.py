import time
startTime=time.clock()

NEEDED=5

        
def run():        
        n=1
        count = 0
        while True:
                x=1
                while len(str(x**n))<=n:
                        if len(str(x**n))==n:
                                count+=1
                                print count, n, x , x**n
                                
                        x+=1
                n+=1


        
        
run()



endTime=time.clock()
print endTime-startTime