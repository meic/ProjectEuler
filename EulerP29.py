import time
startTime=time.clock()

max = 100
min = 2

mylist=[]
for a in range(min,max+1):
        for b in range(min,max+1):
                mylist.append(a**b)


d = {}
for x in mylist:
    d[x] = 1
mylist = list(d.keys())

print len(mylist)

endTime=time.clock()
print endTime-startTime