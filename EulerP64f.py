from math import sqrt, floor

def continued_fraction (n):

    m = [ 0 ]
    d = [ 1 ]
    a = [ int (floor (sqrt (n))) ]

    def terminate ():
        for i in xrange (len (a) - 1):
            if m[i] == m[-1] and d[i] == d[-1] and a[i] == a[-1]:
                return True
        return False

    while not terminate ():
        m.append (d[-1]*a[-1] - m[-1])
        d.append ((n - m[-1]**2)/d[-1])
        a.append (int (floor ((sqrt (n) + m[-1])/d[-1])))
    
    return (len (a) - 2,a[:-1])                  # hackish

print continued_fraction (3)
    
print sum (continued_fraction (n)[0] % 2 == 1
           for n in xrange (1, 10000 + 1)
           if int (sqrt (n)) != sqrt (n))