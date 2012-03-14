import time
startTime=time.clock()

a=1
b=1
carryOn=1
products=[]
sets=[]

for a in range(1,100):
        #print a
        aList=[int(ch) for ch in str(a)]
        #check for duplicates
        for ch in aList:
                if aList.count(ch)>1:
                        carryOn=0
                        break
                
        if carryOn==1:
                #print carryOn
                for b in range(1,10000):
                        #print b
                        c=a*b
                        bList=[int(ch) for ch in str(b)]
                        cList=[int(ch) for ch in str(c)]
                        abcList=aList+bList+cList
                        if len(abcList)==9 and 0 not in abcList:
                                #print carryOn
                                for ch in abcList:
                                        if abcList.count(ch)>1:
                                                carryOn=0
                                                break
                                if carryOn==1:
                                        #print b
                                        products.append(c)
                                        sets.append([a,b,c])
                        carryOn=1                
        carryOn=1                
d = {}
for x in products:
    d[x] = 1
products = list(d.keys())

print products
print sets
print reduce(lambda x,y:x+y , products)


endTime=time.clock()
print endTime-startTime