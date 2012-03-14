import time
startTime=time.clock()

list=[]
n=1

while len(list)<1000000:
        for ch in str(n):
                list.append(int(ch))
        n+=1
# print list
print list[1-1]*list[10-1]*list[10**2-1]*list[10**3-1]*list[10**4-1]*list[10**5-1]*list[10**6-1]

endTime=time.clock()
print endTime-startTime