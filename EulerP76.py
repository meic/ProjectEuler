
maxim = 100

sum = [maxim-1,]
count = 1

def nextSum(sum):
        if sum[-1] == 2:
                return sum[:-1]
        sum[-1] -= 1
        
        while maxim - reduce(lambda x,y:x+y ,sum)>1:
                sum.append( min(maxim - reduce(lambda x,y:x+y ,sum), sum[-1]) )
                
        return sum
                

while sum !=[]:
        #print sum
        sum = nextSum(sum)
        count +=1
        
print count 