import time
startTime=time.clock()

doublePals=[]
count=0
binNo=[]
max=1000000

for x in range(1,max):
        good = 1
        for i in range(len(str(x))/2):
                if str(x)[i]!=str(x)[-1-i]:
                        good=0
                        break
        if good:
                binNo=str(bin(x))[2:]
                for i in range(len(binNo)/2):
                        if binNo[i]!=binNo[-1-i]:
                                good=0
                                break
        if good:
                print "%i    %s"%(x,binNo)
                doublePals.append(x)
                count+=1
                
print sum(n for n in doublePals)
print count
print len(doublePals)


endTime=time.clock()
print endTime-startTime