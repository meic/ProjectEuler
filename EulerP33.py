import time
startTime=time.clock()

list=[]

for num in range(10,100):
        numList=[int(x) for x in str(num)]

        for den in range(10,100):
                denList=[int(x) for x in str(den)]
                
                for x in numList:
                        if x in denList:
                                if denList[denList.index(x)-1] != 0:
                                        if float(numList[numList.index(x)-1])/denList[denList.index(x)-1] == float(num)/den:
                                                list.append([num,den])

for i in range(len(list)):
        print "%i/%i" % (list[i][0],list[i][1])

# 49/98  16/64   19/95   26/65
        
endTime=time.clock()
print endTime-startTime