import time
startTime=time.clock()

n_1=1
n_2=1
n=0

count=2

digits=1000
max=10**(digits-1)

while True:
        # print "%i    %i" % (count,n)
        n=n_1+n_2
        n_2=n_1
        n_1=n
        count+=1
        if n>max:break
        
print "%i    %i" % (count,n)
        
endTime=time.clock()
print endTime-startTime