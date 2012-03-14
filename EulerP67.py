import time
startTime=time.clock()

f = open(".\EulerP67.data","r")

tri = []

#print tri

for i in range(100):
        lineStr=f.readline()
        lineListStr=lineStr.split(" ")
        line=[int(x) for x in lineListStr]
        tri.append(line)
  
while len(tri)>1:  
        for x in range(len(tri[-2])):
                if tri[-1][x]>tri[-1][x+1]:
                        tri[-2][x] += tri[-1][x]
                else:
                        tri[-2][x] += tri[-1][x+1]
        tri.pop()
        
print tri[0][0]
        
endTime=time.clock()
print endTime-startTime