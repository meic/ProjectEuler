import primes


L = 12000 + 1
phi = range(L)
for n in range(2, L):
  if phi[n] == n:
    for k in range(n, L, n):
      phi[k] *= (n - 1.)/n;
 
print "Answer to PE72 =", int(sum(phi)-1)

