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

def getAn(a,n):
        if n == 0: return a[0]
        
        return a[ (n-1)%(len(a)-1) + 1 ]
        
        
def getHorK(a,n,h_1,h_2):
        return getAn(a,n)*h_1 + h_2
        
def genHKs(N):
        (dummy, a) = continued_fraction (N)
        h_2, h_1 = 0,1
        k_2, k_1 = 1,0
        n=0
        while True:
                h = getHorK(a,n,h_1,h_2)
                k = getHorK(a,n,k_1,k_2)
                yield n, getAn(a,n), h, k
                h_2 = h_1
                k_2 = k_1
                h_1 = h
                k_1 = k
                n+=1
                
largestH = 0
corroD=0
for D in range(2,1001):
        if int (sqrt (D)) != sqrt (D):
                for n,an, h, k in genHKs(D):
                        # print n,an, h, k
                        if h**2 - D*k**2==1:
                                if h>largestH:
                                        largestH=h
                                        corroD = D
                                        print h,D,k
                                break
print largestH , corroD
