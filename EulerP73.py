from Euler import gcd
 
L = 12000+1
c = 0
for n in range(5, L):
  for k in range(n/3 + 1, (n-1)/2 + 1):
    if gcd(n,k) == 1: c+=1
 
print "Answer to PE73 =", c