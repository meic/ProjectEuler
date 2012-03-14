import time
import math
startTime=time.clock()

def nextA(h_1,h_2,k_1,k_2,N,Nsqrtin ):
        return -int((- h_1*h_2 + N*k_1*k_2 + math.sqrt(N)*(k_2*h_1 - k_1*h_2)) / (- N * k_2**2 + h_2**2))
        
def testXYD(x,y,D):
        if (x**2 -D* y**2 == 1):
                return True
        return False

def CF_of_sqrt(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        up to (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.mcs.surrey.ac.uk/Personal/R.Knott/Fibonacci/cfINTRO.html
        In the section named: "Methods of finding continued
        fractions for square roots"
    """
    if int(math.sqrt(n))**2 ==n:
        return [int(math.sqrt(n))]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
        ans.append(int(nextn))

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
            ans.append(ans[0] * 2)
            break

        step1_num, step1_denom = step3_num, step3_denom

    return ans
        
def find(n,ans):
        
        if math.sqrt(n)**2 == n:
                return 0,0,0
        
        a = Nsqrtin= int(math.sqrt(n))
        h_2 = 0
        h_1 = 1
        k_2 = 1
        k_1 = 0
        
        count = 0
        while True:
                if count == 0:
                        a=ans[0]
                else:
                        x = (count-1) % (len(ans)-1)
                        a = ans[x+1]
                
                # print n, 'a='+str(a)
                h = a*h_1 + h_2
                k = a*k_1 + k_2
                if testXYD(h,k,n):
                        return h , k, n
                h_2 = h_1
                h_1 = h
                k_2 = k_1
                k_1 = k
def run():
        maxx = 0
        corroD=0
        num=20
        for n in range(2,num+1):
                a = CF_of_sqrt(n)
                if len(a)>1:
                        print n
                        x,y,D = find(n,a)
                        if x>maxx:
                                maxx=x
                                corroD=D
                                print x , D
        print corroD
                
run()



endTime=time.clock()
print endTime-startTime