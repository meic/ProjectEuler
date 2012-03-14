import time
startTime=time.clock()

rangeBegin=500000
rangeEnd=1000000

currentList=[]
dic={}

for startNo in range(rangeBegin,rangeEnd+1):

        #print startNo
        currentList=[]
        n=startNo
        count = 0
        
        while n !=1:
                if dic.has_key(n):
                        count = dic[n]
                        n=1
                elif n % 2 ==0:
                        currentList.append(n)
                        n=n/2
                else:
                        currentList.append(n)
                        n=3*n +1
        
        for x in range(len(currentList)):
                dic[currentList[-1-x]]=count+x+1
        
maxLength=max(dic.values())
for key in dic.keys():
        if dic[key]==maxLength: print key

                
endTime=time.clock()
print endTime-startTime