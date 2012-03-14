n=7

n=500
count=0
while count<=500:
        tri = n*(n+1)/2
        #print tri
        count = 0
        for x in range(1,tri+1):
                if tri % x == 0:
                        count+=1
        #print n
        n += 2
print n
print tri