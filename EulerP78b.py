import primes

s = [primes.prime(x) for x in range(50)]

def find(target):
        ways = [1]+[0]*target
        
        for s_i in range(1,target):
                if s_i < target:
                        for i in range(s_i,target+1):
                                ways[i] += ways[i - s_i]
                                
                                if (ways[s_i]+1)%10**6==0:
                                        return s_i+1
                                


print find(10**6)           
