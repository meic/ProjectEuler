
maxim = 9

w=[0,1,]+[0,]*(maxim-1)
print len(w)
for n in range(2,maxim+1):
        for i in range(1,n):
                print n, i, n-i
                w[n]+=w[i]*w[n-i]
print w