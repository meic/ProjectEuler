import time
startTime=time.clock()

right = 1

for x in range(182,500):
        right =1
        list=[int(ch) for ch in str(x)]
        list.extend([int(ch) for ch in str(2*x)])
        for i in range(2,8):
                if not list.count(i)==1:
                        right =0
                        break
        if right==1:
                print list
                print x
                        
        # if right == 1:
                # break

# print list



endTime=time.clock()
print endTime-startTime