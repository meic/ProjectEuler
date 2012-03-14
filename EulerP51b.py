import time
import primes
startTime=time.clock()
Amount=8

# strNos=[str(i) for i in range(10)]
def listToNum(mylist):
        sum=0
        for i in range(len(mylist)):
                sum+= mylist[-1-i]*10**i
        return sum
        
##for 2 digits
# contin=1
# x=10
# while contin:
        # prime=[int(i) for i in str(primes.prime(x))]
        # for i in range(len(prime)-1):
                # for j in range(i+1):
                        # list2=list(prime)
                        # count=0
                        # for k in range(10):
                                # list2[i+1]=list2[j]=k
                                # if primes.isprime(listToNum(list2)) and listToNum(list2)>999:
                                        # count+=1
                                        # if count==Amount:
                                                # print listToNum(prime)
                                                # contin=0
        # x+=1
        
##for 3 digits
contin=1
x=25
while contin:
        prime=[int(i) for i in str(primes.prime(x))]
        for i in range(len(prime)-2):
                for j in range(i+2):
                        for jj in range(j+1):
                                # if jj==0:
                                        # am=Amount+1
                                # else
                                        
                                list2=list(prime)
                                count=0
                                for k in range(10):
                                        list2[i+2]=list2[j+1]=list2[jj]=k
                                        if primes.isprime(listToNum(list2)) and list2[0]!=0:
                                                count+=1
                                                if count==Amount:
                                                        print listToNum(prime)
                                                        print i+2
                                                        print j+1
                                                        print jj
                                                        for k in range(10):
                                                                list2[i+2]=list2[j+1]=list2[jj]=k
                                                                if primes.isprime(listToNum(list2)) and list2[0]!=0:
                                                                        print listToNum(list2)
                                                        contin=0
        x+=1

        
        


endTime=time.clock()
print endTime-startTime