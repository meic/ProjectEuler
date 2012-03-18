
def h(a,k,m):
        if k==1: return a
        return pow(a,h(a,k-1,m),10**m)
        
print h(3,3,4) # method hits max reccursion depth for below numbers

k =1855
a = 1777
m = 8
curr = 1
for i in range(k+1,1,-1):
        curr = pow(a,curr,10**m)
        
print curr
