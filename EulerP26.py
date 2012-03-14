import time
startTime=time.clock()

max= 1000
def div(x,y):
        d=int(x/y)
        r=x%y
        return d,r
leng=0
maxLeng=0
number=0
for x in range(1,max+1):
        d=10
        list=[]
        while True:
                z,d=div(d,x)
                if d==0: break
                if d in list:
                        leng=len(list)-list.index(d)
                        if leng>maxLeng: 
                                maxLeng=leng
                                number = x
                        # print leng
                        break
                list.append(d)
                d=d*10
print maxLeng
print number
        
endTime=time.clock()
print endTime-startTime