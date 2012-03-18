import primes

s = [primes.prime(x) for x in range(50)]

def find(target):
        ways = [1]+[0]*target
        
        for s_i in s:
                if s_i < target:
                        for i in range(s_i,target+1):
                                ways[i] += ways[i - s_i]
        
        return ways[target]


x = 11
while True:
        if find(x)>=5000:
                print x
                break
        x+=1
                
