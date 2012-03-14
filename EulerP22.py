import time
startTime=time.clock()

f = open(".\EulerP22.data","r")

names = []

lineStr=f.readline()
#print lineStr

names=lineStr.split('","')



# def compair(name1, name2):
        # for x in range(min(len(name1),len(name2))):
                # if ord(name1[x])>ord(name2[x]): return False
                # elif ord(name1[x])<ord(name2[x]): return True
        # if len(name1)<len(name2): return True
        # else: return False
        
# loopThrough=1
# while loopThrough!=0:
        # loopThrough=0
        # for x in range

names.sort()

def nameSum(name):
        sum=0
        for ch in name:
                sum+=ord(ch)-64
        return sum

#print nameSum("COLIN")
total=0

for i in range(len(names)):
        total += nameSum(names[i])*(i+1)
        #print i

print total
   
#print ord(names[10][0])
        
endTime=time.clock()
print endTime-startTime