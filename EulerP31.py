import time
startTime=time.clock()

coins=[100,50,20,10,5,2,1]
count =2
list=[100,100]

def removeOne(mylist,last):
        if last==5:
                mylist.extend([2,2])
        if last==10:
                mylist.extend([5,2,2])
        if last==20:
                mylist.extend([10,5,2,2])
        if last==50:
                mylist.extend([20,20,5,2,2])
        if last==100:
                mylist.extend([50,20,20,5,2,2])
        return mylist

while list:
        lastCoin=list.pop()
        if lastCoin!=2:
                list=removeOne(list,lastCoin)
        count += 1
        print count
        print list
        # print "%i     %l" % (count,list)
print count
endTime=time.clock()
print endTime-startTime