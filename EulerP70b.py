from Euler import prime_sieve, is_perm, sqrt
 
min_q, i, L = 2, 0, 10**7
primes = prime_sieve(1.30*sqrt(L))
ll = 0.7*sqrt(L)
for n in range(len(primes)):
  if primes[n]>ll: break
del primes[:n]
 
for p1 in primes:
  i+=1
  for p2 in primes[i:]:
    n = p1 * p2
    if n > L: break
    phi = (p1-1) * (p2-1)
    q = n / float(phi)
    if is_perm(phi, n) and min_q>q: min_q, min_n = q, n
 
print "Answer to PE70 = ",min_n