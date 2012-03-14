import time
startTime=time.clock()


def run():
        maxSum=0
        for a in range(1,100):
                for b in range(1,100):
                        mylist=[int(x) for x in str(a**b)]
                        sum=reduce(lambda x,y:x+y, mylist)
                        if sum>maxSum:maxSum=sum
        print maxSum

run()



endTime=time.clock()
print endTime-startTime