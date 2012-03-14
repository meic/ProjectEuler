from math import factorial

def next(x):
        sum=0
        for i in [int(ch) for ch in str(x)]:
                sum+= factorial(i)
        return sum
        
loops = {169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}

def findLeng(x):
        count = 0
        while True:
                if x in loops:
                        return count + loops[x]
                count +=1
                next_x = next(x)
                if x == next_x:
                        return count
                x = next_x

maxim = 10**6

count =0
for i in range(2,maxim+1):
        if i%10**4==0: print i/10**4
        if findLeng(i) == 60:
                count +=1
print count
