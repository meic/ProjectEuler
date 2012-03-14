maxL = 1500000

count =0
for L in range(2,maxL+1):
        subCount=0
        for x in range(1,L/2):
                if (L*(L-2*x))%(2*(L-x)) == 0:
                        subCount+=1
        if subCount==2:
                count +=1
                if L%10000==0:
                        print L,count
                        
print count