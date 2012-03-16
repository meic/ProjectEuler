
def count( n, m ):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0
 
    return count( n, m - 1 ) + count( n - m, m )

target = 100
print count(target,target - 1)